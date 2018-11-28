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


//22: 3 2 3
//23: 3 3 2
//29: 2 3 3

//=========================================================
// program:
//
struct solver
{
    const string BAD = "zzz";
    
    map< pair<pair<int,char>, pair<int,int> >, string > memo;
    
    string solve(int N, int R, int P, int S, char winner)
    {
        if (N == 0) {
            if (R == 1 && winner == 'R') {
                return "R";
            }
            if (P == 1 && winner == 'P') {
                return "P";
            }
            if (S == 1 && winner == 'S') {
                return "S";
            }
            return BAD;
        }
        
        if (memo.count( { {N,winner}, {R,P} } ) == 1 ) {
            return memo[ { {N,winner}, {R,P} } ];
        }
        
        int a, b, c;
        if ( (1 << N) % 3 == 2) {
            a = (1 << N) / 3;
            b = (1 << N) / 3 + 1;
            c = (1 << N) / 3 + 1;
        } else {
            a = (1 << N) / 3;
            b = (1 << N) / 3;
            c = (1 << N) / 3 + 1;
        }
        vector<int> req = {a,b,c};
        string res = BAD;
        do {
            if (req[0] == R && req[1] == P && req[2] == S) {
                char p = winner, q;
                if (p == 'R') {
                    q = 'S'; 
                } 
                if (p == 'S') {
                    q = 'P'; 
                } 
                if (p == 'P') {
                    q = 'R'; 
                } 
                
                for (int o1 = 0; o1 < 3; o1++) {
                    for (int o2 = 0; o2 < 3; o2++) {
                        int t = 1 << (N - 1);
                        
                        int def = t/3;
                        if (t % 3 == 2) {
                            def++;
                        }
                        vector<int> rps1(3, def);
                        vector<int> rps2(3, def);
                        
                        if (t % 3 == 2) {
                            rps1[o1]--;
                            rps2[o2]--;
                        } else {
                            rps1[o1]++;
                            rps2[o2]++;
                        }
                        int r1 = rps1[0], p1 = rps1[1], s1 = rps1[2];
                        int r2 = rps2[0], p2 = rps2[1], s2 = rps2[2];
                        
                        
                        if ( (r1 + r2 == R) && (s1 + s2 == S) && (p1 + p2 == P) ) {
                            // p,q
                            string res1 = solve(N-1, r1, p1, s1, p);
                            string res2 = solve(N-1, r2, p2, s2, q);
                            
                            if (res1 != BAD && res2 != BAD) {
                                res = std::min(res, res1 + res2);
                            }
                            
                            res1 = solve(N-1, r1, p1, s1, q);
                            res2 = solve(N-1, r2, p2, s2, p);
                            if (res1 != BAD && res2 != BAD) {
                                res = std::min(res, res1 + res2);
                            }

                        }
                    
                    
                    }
                }

            }
        } while (next_permutation(req.begin(), req.end()) );
        
        memo[ { {N,winner}, {R,P} } ] = res;
        return res;
        
    }
    string solve(int N, int R, int P, int S)
    {
        string res = std::min( {solve(N, R,P,S, 'P'),solve(N, R,P,S, 'R'), solve(N, R,P,S, 'S') } );
        
        if (res == BAD) {
            return "IMPOSSIBLE";
        } else {
            return res;
        }
    }

    void init() { }
    
    int N,R,P,S;
    void read() {
        cin >> N >> R >> P >> S;
    }
    #if MAX_THREADS > 1
        ofstream cout;
    #endif
    void write(int cn) {
        cout << "Case #"<<cn<<": " << solve(N,R,P,S) << endl;
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
