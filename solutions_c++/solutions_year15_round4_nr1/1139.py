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
    int R, C;
    char board[100][100];
    
    int solve()
    {
        int dx[4]      = {0,0,-1,1};
        int dy[4]      = {-1,1,0,0};
        const char* dc = "<>^v";
        map<char, int> cd;
        for (int i = 0; i < 4; i++) {
            cd[ dc[i] ] = i;
        }
        
        int allowed_mask[100][100];
        /*cout << endl;*/
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                //cout << board[i][j];
                allowed_mask[i][j] = 15;
            }
            //cout << endl;
        }
        // Over engineering , your name is me.
        for (int d = 0; d < 4; d++) {
            int N, M;
            if (dx[d] == 0) {
                N = R, M = C;
            } else {
                M = R, N = C;
            }
            
            for (int i = 0; i < N; i++) {
                int ini, end, inc;
                if (dx[d] + dy[d] > 0) {
                    ini = 0;
                    end = M;
                    inc = 1;
                } else{
                    ini = M-1;
                    end = -1;
                    inc = -1;
                }
                int x = i, y = -1;
                for (int j = ini; j != end; j += inc) {
                    if (dx[d] == 0) {
                        if (board[i][j] != '.') {
                            y = j;
                        }
                    } else {
                        if (board[j][i] != '.') {
                            y = j;
                        }
                    }
                }
                if (y != -1) {                 
                    if (dx[d] != 0) {
                        swap(x,y);
                    }
                    allowed_mask[x][y] ^= (1 << d);
                    //cout << d << ", "<<i<<", "<<" , "<<x<<", "<<y<<" " << board[x][y] << endl;
                }
                
            }
        }
        int cost = 0;
        
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (board[i][j] != '.') {
                    if ( allowed_mask[i][j] == 0) {
                        return -1;
                    }
                    int d = cd[ board[i][j] ];
                    if ( ! ( (1 << d) & allowed_mask[i][j] ) ) {
                        //cout << i << ", "<<j<<" cannot be "<<dc[d] << " " << allowed_mask[i][j] << endl;
                        cost++;
                    } else {
                        //cout << i << ", "<<j<<" can be "<<dc[d] << " " << allowed_mask[i][j] << endl;
                    }
                }
            }
        }
        return cost;
    }
    void init() { }
    void read() {
        cin >> R >> C;
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                cin >> board[i][j];
            }
        }
    }
    #if MAX_THREADS > 1
        ofstream cout;
    #endif
    void write(int cn) {
        cout << "Case #"<<cn<<": ";
        int x = solve();
        if (x == -1) {
            cout << "IMPOSSIBLE";
        } else {
            cout << x;
        }
        cout <<endl;
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
