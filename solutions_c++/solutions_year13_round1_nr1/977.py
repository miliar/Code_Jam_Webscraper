/*******************************************************************
*                          CODE JAM 2013
*                    ROUND:                 1A 
*                       CONTESTER:  yi
*                           Problem: A
*******************************************************************/
 
// headers
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

#include <omp.h>
#include <gmp.h>
#include <gmpxx.h>


//DEBUGING

#ifdef DEBUG
#define ASSEART(X)     if (!(X)) {printf("\n %s: assertion failed at line %d\n",__FILE__,__LINE__);exit(0);} 
#define PRINT(fmt, args...) printf("%s:%s:%d: "fmt, __FILE__, __FUNCTION__, __LINE__, args); 
#define PVAR(var) cout<<__FILE__<<":"<<__FUNCTION__<<":"<<__LINE__<<":    "<<#var<<" = "<<var<<endl;
#define PLINE(array,n) \
printf("\n%s:%s:line %d : "#array"[0:%d]=\n",__FILE__, __FUNCTION__, __LINE__,n);\
for(register size_t __i__=0;__i__<n;__i__++) \
    cout<<__i__<<" ";\
cout<<endl;\
for(register size_t __i__=0;__i__<n;__i__++) \
        cout<<array[__i__]<<" ";\
        cout<<endl;
#define PMAP(array,n,m,fmt) {\
printf("%s:%s:line %d : "#array"[0:%d][0:%d]=\n",__FILE__, __FUNCTION__, __LINE__,n,m);\
cout<<"  ";\
for(register size_t __j__=0;__j__<m;__j__++) \
cout<<__j__;\
cout<<endl;\
for(register size_t __i__=0;__i__<n;__i__++) {\
    cout<<__i__;\
    for(register size_t __j__=0;__j__<m;__j__++) \
        printf(fmt,array[__i__][__j__]);\
    cout<<endl;\
}\
}
#define PBIN(n) {\
        int i,bit[256];\
        for(i=0;i<sizeof(n)*8;i++) {bit[i]=n%2;n>>=1;}\
        for(;i>0;i--) {cout<<bit[i-1];}\
    }
#define EVAL(cmd) cmd
#else
#define PMAP(array,n,m,fmt) 
#define ASSEART(X)
#define PVAR(var)
#define PRINT(fmt, args...) 
#define PLINE(array,n)
#define PBIN(n)
#define EVAL(cmd)
#endif
//Helpers
#define repeat(n,__i__) for(register size_t __i__=0;__i__<n;__i__++) 
#define all(cnt) cnt.begin(),cnt.end()
#define forall(cnt,it) for(typeof(cnt.begin()) it=cnt.begin();it!=cnt.end();it++)
#define RCMAP(array,n,m) \
    for(register size_t __i__=0;__i__<n;__i__++) {\
        string __l__;\
        getline(cin,__l__);\
        for(register size_t __j__=0;__j__<m;__j__++) {\
            array[__i__][__j__]= __l__[__j__];\
        }\
    }
#define RMAP(array,n,m) \
    for(register size_t __i__=0;__i__<n;__i__++) {\
        string __l__;\
        getline(cin,__l__);\
        for(register size_t __j__=0;__j__<m;__j__++) {\
            istringstream(__l__)>>array[__i__][__j__];\
        }\
    }
typedef long long ll;

//Possible Template classes (Graph, Geometric...).         

//Test Case 
class TestCase {
    //Helpers
//    inline readMap(int N,M) {};
    //static const int Limit=1;
    
    //variables list
    mpz_class r,n,t;
    //Implement details
    
public:
    //Input
    TestCase(istream& input) {
        init(input);
    }
    //TestCase(i,j,k) : N(i),J(j),K(k) {};
    template<class _stream>
    void init(_stream& input=cin) {
        string rs,ts,line;
        getline(input,line);
        rs=line.substr(0,line.find(' ')+1);
        ts=line.substr(line.find(' ')+1,line.size());
        r=mpf_class(rs);
        t=mpz_class(ts);
    };
    //solve the problem
    void solve() {
        //TEST input first?
        mpf_class rf=mpf_class(r.get_str(10));
        mpf_class tf=mpf_class(t.get_str(10));
        rf.set_prec(512);
        tf.set_prec(512);
        mpf_class tmp;
        tmp.set_prec(512);
        tmp=(sqrt((2*rf-1)*(2*rf-1)+8*tf)-(2*rf-1))/4;
        n=mpz_class(tmp.get_ui());
        PVAR(n);
        while(2*n*n + (2*r-1)*n < t) {
            n++;
        }
        while(2*n*n + (2*r-1)*n > t) {
            n--;
        }
        return ;
    };
    //format output
    string result() {
        
        return n.get_str(10);
    };
};
    
// ------------------------ Start @ Fri Apr 26 20:56:23 EDT 2013 ---------------------------------------

int main() {
    int nCase;
    string line;
    getline(cin,line);
    istringstream(line)>>nCase;
    vector<TestCase> testcases;
    for(int i=0;i<nCase;i++) testcases.push_back(TestCase(cin));
#pragma omp parallel for num_threads(4)
    for(int i=0;i<nCase;i++) testcases[i].solve();
    for(int i=0;i<nCase;i++) cout<<"Case #"<<i+1<<": "<<testcases[i].result()<<endl;

}

//Statistics

//------- finished small at Fri Apr 26 22:12:43 EDT 2013--------------
//------- finished large at Fri Apr 26 22:13:37 EDT 2013--------------
