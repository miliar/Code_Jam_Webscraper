#ifdef VX_PRECOMPILED
    #include "precomp.h"
    typedef mpz_class big;
    // I use 4 cores :)
    #define MAX_THREADS 4
#else
    #include<string>
    #include<iostream>
    #include<fstream>
    #include<sstream>
    #include<assert.h>
    #include<cstdio>
    #include<map>
    #include<algorithm>
    #include<bitset>
    #include<cmath>
    #include<queue>
    #include<functional>
    #include<set>
    #include<sys/stat.h>
    #include<numeric>
    #include<cstdio>
    #include<cstdlib>
    #include<cstring>
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

#include<stack>

//=========================================================
// program:
//
struct solver
{
    long solve1(int N, long P)
    {
        long T = (1LL<<N);
        if (P == T) {
            return T-1;
        }
        T /= 2;
        long k = 1;
        long c = 1;
        while (T > 0) {
            if (c + T > P) {
                return k - 1;
            }
            c += T;
            k = 2*k + 1;
            T /= 2;
        }
        return -1;
        
        

    }
    long solve2(int N, long P)
    {
        long T = (1LL << N);
        if (P == T) {
            return T-1;
        }
        // T - solve1(N,T-P) - 1 returns guaranteed to lose 
        return T - solve1(N, T-P) - 2;
    }
    
    void init() {/*
        const int K = 8;
        for (int P=0; P<=K; P++) {
            cout << "P = "<<P<< " : " ;
            int x[K];
            for (int i=0; i<K; i++) {
                x[i] = i;
            }
            vector<bool> wins(K, true);
            do {
                vector<int> results[K*2-1];
                for (int i=0; i<K; i++) {
                    results[0].push_back(x[i]);
                }
                for (int i=0; i<K-1; i++) {
                    for (int j=0; j<results[i].size(); j+=2) {
                         if (results[i][j] > results[i][j+1]) {
                             results[i*2+1].push_back(results[i][j+1]);
                             results[i*2+2].push_back(results[i][j]);
                         } else {
                             results[i*2+1].push_back(results[i][j]);
                             results[i*2+2].push_back(results[i][j+1]);
                         }
                    }
                }
                for (int i=K-1 + P; i<2*K-1; i++) {
                    wins[ results[i][0] ] = false;
                }
            } while ( next_permutation(x,x+K));
            for (int i=0; i<wins.size(); i++) cout << (wins[i]?'W':'L');
            cout << endl;
        }
    */
    
    }
    int N;
    long P;
    void read() {
        cin >> N >> P;
    }
    #if MAX_THREADS > 1
        ofstream cout;
    #endif
    void write(int cn) {
        cout << "Case #"<<cn<<": "<<solve1(N,P)<<" " <<solve2(N,P) << endl;
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
