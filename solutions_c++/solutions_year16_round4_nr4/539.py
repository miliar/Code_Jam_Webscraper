#ifdef VX_PRECOMPILED
    #include "precomp.h"
    typedef mpz_class big;
    // I use 4 cores :)
    #define MAX_THREADS 4
#else
    #include <bits/stdc++.h>
    #include<sys/stat.h>
    #include<unistd.h>
    // http://gmplib.org/ (uncomment if solution uses big nums)
    // most likely you'll get an error about mpz_class not being declared...
    //#include "gmpxx.h"
    #define big mpz_class
    // I figure that when other people want to test my solutions they shouldn't
    // get the whole multi-threaded mess that requires and deletes folders and files...
    #define MAX_THREADS 1
#endif

#define for_each(q,s) for(typeof(s.begin()) q=s.begin(); q!=s.end(); q++)
typedef long long int64;
#define long int64

using namespace std;

//=========================================================
// program:
//
struct solver
{
    int N;
    vector<string> adj;
    
    bool completely_good(vector<string> & A)
    {
        vector<int> workers(N);
        for (int i = 0; i < N; i++) {
            workers[i] = i;
        }
        do {
            vector<int> machines(N);
            for (int i = 0; i < N; i++) {
                machines[i] = i;
            }
            do {
                vector<bool> used_machines(N, false);
                for (int i = 0; i < N; i++) {
                    int x = workers[i]; // x enters factory
                    int p = -1;
                    for (int j = 0; j < N; j++) {
                        int y = machines[j];
                        if (! used_machines[y] && (A[x][y] == '1') )  {
                            p = y;
                            break;
                        }
                    }
                    if (p == -1) {
                        return false;
                    }
                    used_machines[p] = true;
                }
            } while (next_permutation(machines.begin(), machines.end()) );
        } while (next_permutation(workers.begin(), workers.end()) );
        
        return true;
    }
    
    int solve()
    {
        int res = N*N;
        for (int mask = 0; mask < (1 << (N*N)); mask++) {
            vector<string> A = adj;
            int c = 0;
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if ( !( (adj[i][j] == '0' || adj[i][j] == '1') ) ) {
                        cerr << "["<<adj[i][j] <<"]"<<endl;
                        assert(false);
                    }
                    if ( (adj[i][j] == '0') && (mask & ( 1 << (i*N+j) ) ) ) {
                        A[i][j] = '1';
                        c++;
                    }
                }
            }
            
            if ( completely_good(A)) {
                res = std::min(res, c);
            }
        }
        return res;
    }
    void init() { }
    void read() {
        cin >> N;
        adj.resize(N);
        for (string &x : adj) {
            cin >> x;
        }
        
    }
    #if MAX_THREADS > 1
        ofstream cout;
    #endif
    void write(int cn) {
        cout << "Case #"<<cn<<": " << solve() << endl;
    }
    
};

//=========================================================
// I/O:
//
#if MAX_THREADS > 1
    void run(const char* x)
    {
        int r = system(x);
        cerr<<x<<" "<<"("<<r<<")"<<endl;
    }
#endif

int main(int argc, const char* argv[])
{
    int TestCases, mode;
    #if MAX_THREADS == 1
        // Simple and straight forward. 
        cin >> TestCases;
        solver * theSolver = new solver;
        theSolver->init();
        for (int i=1; i<= TestCases; i++) {
            theSolver->read();
            theSolver->write(i);
        }
        delete theSolver;    
    #else
        cin>>TestCases;
        //-------------------------------------------
        // Copy the whole input to a file...
        ofstream f;
        f.open("tests/.input");
        f << cin.rdbuf();
        f.close();
        // Yeah...wipe that folder... Cause we will need its files to be empty
        run("rm ./tests/.t*");
        int k = 0;
        mode = 0;
        // We create some extra threads...
        while (k < MAX_THREADS) {
            if ( fork() == 0 ) {
                mode = k + 1;
                break;
            }
            k++;
        }
        // Reopen the input, this happens for each of the threads...
        if (mode != 0) {
            assert( freopen( "tests/.input","r",stdin) );
        }
    
        solver * theSolver = new solver;
        theSolver->init();
        for (int i=1; i<= TestCases; i++) {
            // Yeah, I don't like this much either
            ofstream f;
            char fn1[200], fn2[200];
            sprintf(fn1, "tests/.test.%d", i);
            sprintf(fn2, "tests/.test.%d.done", i);
            if (mode == 0) {
                // main thread shall just join stuff together as it becomes ready
                struct stat stFileInfo;
                // When a thread finishes a test case, it writes the .done file
                // Wait for that...
                while ( stat(fn2, &stFileInfo) !=0 ) {
                    sleep(1);
                }
                // Now copy the output file...
                ifstream f(fn1);
                cout << f.rdbuf();
            } else {
                // The trick is to make each thread read all the inputs, whether
                // it will process it or not...
                theSolver->read();
                // If fn1 exists, it is being processed already. Else process it
                f.open(fn1, ios_base::out | ios_base::in);
                if ( !f ) {
                    theSolver->cout.open(fn1, ios_base::out);
                    cerr << "[" << i << "/"<<TestCases<<"] "<<mode << endl;
                    theSolver->write(i);
                    theSolver->cout.close();
                    f.open(fn2);
                    f << "1" << endl;
                }
            }
        }
        delete theSolver;
    #endif

    
    return 0;
}
