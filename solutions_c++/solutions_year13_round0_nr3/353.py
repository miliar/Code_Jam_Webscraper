#ifdef VX_PRECOMPILED
#include "precomp.h"
typedef mpz_class big;
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
// http://gmplib.org/ (uncomment if solution does not use big nums)
#include "gmpxx.h"
#define big mpz_class
#endif

#define for_each(q,s) for(typeof(s.begin()) q=s.begin(); q!=s.end(); q++)
typedef long long int64;
#define long int64
// Number of concurrent processes solving the input
const int MAX_THREADS = 4;
using namespace std;



//=========================================================
// program:
//
struct solver
{
    void init() { }
    big A, B;

    void read(istream& cin) {
        cin >> A >> B;
    }
    
    char x[100];
    char y[100];
    
    bool palindrome(string s)
    {
        int i = 0, j = s.length() - 1;
        while (i < j) {
            if (s[i] != s[j]) {
                return false;
            }
            i++; j--;
        }
        return true;
    }
    int theCount, lim;

    void find(int len, ostream& cout) {
        bool good = ( len == 0 ) ;
        if (len > 0) for (int k = 0; k < 2; k++) {
            int l2;
            if (k == 0) {
                l2 = len*2 - 1;
            } else {
                l2 = len*2;
            }
            for (int i=0; i < len; i++) {
                y[i] = x[i];
                y[l2 - i - 1] = x[i];
            }
            y[l2] = 0;
            if ( 2 * l2 - 1 <= lim) {
                big z(y, 10);
                big w = z * z;
                if (w <= B) {
                    if ( palindrome(w.get_str()) ) {
                        good = true;
                        if( A <= w) {
                            theCount++;
                        }
                    }
                }
            }
        }
        if(! good) return;
        if (len != 0) {
            x[len] = '0';
            find(len + 1, cout);
        }        
        x[len] = '1';
        find(len + 1, cout);
        x[len] = '2';
        find(len + 1, cout);                
    }

    int solve(ostream & cout)
    {
        lim = B.get_str().length();
        theCount = (A <= 9 && 9 <= B);
        find(0, cout);

        return theCount;
    }
    
    void write(int cn, ostream& cout) {
        cout << "Case #"<<cn<<": "<<solve(cout)<<endl;
    }
    
    
};

//=========================================================
// I/O:
//


void run(const char* x)
{
    int r = system(x);
    cerr<<x<<" "<<"("<<r<<")"<<endl;
}
int main(int argc, const char* argv[])
{
    int TestCases;
    if (MAX_THREADS == 1) {
        //simple mode
        cin >> TestCases;
        solver* s = new solver;
        s->init();
        for (int i=1; i<=TestCases; i++) {
            cerr << "[" << i <<"/" << TestCases << "]"<< endl;
            s->read(cin);
            s->write(i, cout ) ;
        }
        delete s;
        
        return 0; 
    }
    int mode = 0;
    if(argc >= 2) sscanf(argv[1],"%d",&mode);
    
    if ( ( mode == 0 ) && (MAX_THREADS > 1) ) {
        string inputfile = ".input";
        run("cat > .input");
        assert( freopen(inputfile.c_str(),"r",stdin) );

        cin>>TestCases;
        for (int i=1; i<=TestCases; i++) {
            char fn[200];
            sprintf(fn, ".test.%d", i);
            remove(fn);
            sprintf(fn, ".test.%d.out", i);
            remove(fn);
        }
       

        cerr<<"--Multi process mode--"<<endl;
        for (int i = 1; i < MAX_THREADS; i++) {
            string command = argv[0];
            string ch (1, i + '0');
            command += " "+ch+" < "+inputfile+" > .tem &";
            run(command.c_str());
        }
    } else {
        cin>>TestCases;
    }
    solver * theSolver = new solver;
    theSolver->init();
    for (int i=1; i<= TestCases; i++) {
        theSolver->read(cin);
        ofstream f;
        char fn1[200], fn2[200];
        sprintf(fn1, ".test.%d", i);
        sprintf(fn2, ".test.%d.out", i);
        f.open(fn1, ios_base::out | ios_base::in);
        if ( !f ) {
            f.open(fn1, ios_base::out);
            //good, do it
            cerr << "[" << i << "/"<<TestCases<<"] "<<mode << endl;
            theSolver->write(i, f);
            f.close();
            f.open(fn2);
            f << "1" << endl;
        } 
    }
    delete theSolver;
    if (mode == 0) {
        //time to merge results...
        for (int i=1; i<= TestCases; i++) {
            char fn1[200], fn2[200];
            sprintf(fn1, ".test.%d", i);
            sprintf(fn2, ".test.%d.out", i);
            struct stat stFileInfo;
            while ( stat(fn2, &stFileInfo) !=0 ) {
                sleep(1);
            }
            sprintf(fn1, ".test.%d", i);
            ifstream f(fn1);
            cout << f.rdbuf();
        }
    }
    
    return 0;
}
