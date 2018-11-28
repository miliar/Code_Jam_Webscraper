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
    vector<int> BFF;
    
    int solve()
    {
        int res = 0;
        
        // step 1: find simple cycles:
        for (int i = 0; i < N; i++) {
            int j = BFF[i] - 1;
            int s = 1;
            //cout << i << " -> " << j << endl;
            while ( (j != i) && (s < 2*N) ) {
                //cout << j << " -> " << BFF[j]-1 << endl;
                j = BFF[j] - 1;
                s++;
            }
            //cout << endl;              
            if (i == j) {
                res = std::max(res, s);
            }
        }
        
        // step 2: the happy mutual BFFs  o <-> o
        vector<bool> happy(N);
        for (int i = 0; i < N; i++) {
            if ( BFF[BFF[i]-1]-1 == i ) {
                happy[i] = true;
            }
        }
        
        vector<int> happy_tail(N, 0);
        for (int i = 0; i < N; i++) {
            int s = 0;
            int j = i;
            while (! happy[j]) {
                s++;
                j = BFF[j] - 1;
                if (s > 2*N) {
                    break;
                }
            }
            if ( happy[j]) {
                happy_tail[j] = std::max(happy_tail[j], s);
            }
            
        }
        int c = 0;
        for (int i = 0; i < N; i++) {
            if ( happy[i] ) {
                c += happy_tail[i] + 1;
            }
        }
        res = std::max(res, c);
        
        
        
        return res;
    }
    void init() { }
    void read() {
        cin >> N;
        BFF.resize(N);
        for (int i = 0; i < N; i++) {
            cin >> BFF[i];
        }
    }
    #if MAX_THREADS > 1
        ofstream cout;
    #endif
    void write(int cn) {
        int x = solve();
        cout << "Case #"<<cn<<": " << x << endl;
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
