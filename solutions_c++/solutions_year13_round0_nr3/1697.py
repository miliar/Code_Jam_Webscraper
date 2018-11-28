/*******************************************************************
*                          CODE JAM 2013
*                    ROUND:                 Qualification 
*                       CONTESTER:  yi
*                           Problem: C
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
#include <fstream>
using namespace std;

#include <omp.h>
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
    
// ------------------------ Start @  Sat Apr 13 13:54:04 EDT 2013---------------------------------------
bool isFair(mpz_class num) {
    string s=num.get_str(10);
    int l=s.size();
    for(int i=0,j=l-1;i<j;i++,j--) 
        if(s[i]!=s[j]) return false;
    return true;
}



int main() {
    //precalculate 1->10^100
    queue<mpz_class> q;
    vector<mpz_class> fsquare;
    for(int i=1;i<4;i++) {
        q.push(mpz_class(i));
    }
    int l;
    do {
      mpz_class num=q.front();
      string s=num.get_str(10);
      q.pop();
      l=s.size();
      mpz_class sq=num*num;
      if(isFair(sq)) {
        //cout<<sq<<endl;
        fsquare.push_back(sq);
      }
      if(l %2 == 0) {
        for(char i=0;i<4;i++) {
            q.push(mpz_class(string(s).insert(l/2,1,i+'0')));
        }
      } else {
         q.push(mpz_class(string(s).insert(l/2+1,1,s[l/2])));
      }
    } while(l<15);
    int nCase;
    string line;
    getline(cin,line);
    istringstream(line)>>nCase;
    for(int i=0;i<nCase;i++) {
        string line;
        getline(cin,line);
        int k=line.find(" ");
        string first,second;
        first=line.substr(0,k);
        second=line.substr(k+1);
        mpz_class start=mpz_class(first);
        mpz_class end=mpz_class(second);
        int lower=-1,upper=fsquare.size(),n;
        for(int j=0;j< fsquare.size();j++) {
            if (fsquare[j]<start) lower=j;
        }
        for(int j=fsquare.size()-1;j>=0;j--) {
            if (fsquare[j]>end) upper=j;
        }
        n=upper-lower-1;
        cout<<"Case #"<<i+1<<": "<<n<<endl;
    }

}

//Statistics

//------- finished small at Sat Apr 13 14:02:17 EDT 2013--------------
//------- finished small at Sat Apr 13 14:02:52 EDT 2013--------------
//------- finished large at Sat Apr 13 14:15:29 EDT 2013--------------
