/*
 *Aditya Gourav @ adi.pearl
 */
#include<bits/stdc++.h>
using namespace std;

///scanning
#define si(x) scanf("%d",&x)
#define ss(x) scanf("%s",x)
#define ssWSP(x) scanf(" %[^\r\n]",x)
#define sill(x) scanf("%lld",&x)
#define sd(x) scanf("%lf",&x)

///debugging
struct debugger{template<typename T> debugger& operator,(const T& v){cerr<<v<<" ";return *this;}}dbg;
#define db(args...) do {cerr << #args << ": "; dbg,args; cerr << endl;} while(0)

///others
#define FI(var,beg,end) for(int var=(beg);var<=(end);++var)
#define FIA(var,beg,end,inc) for(int var=(beg);var<=(end);var+=(inc))
#define FD(var,end,beg) for(int var=(end);var>=(beg);--var)
#define F(i,n) FI(i,0,n-1)
#define F1(i,n) FI(i,1,n)
#define SZ(x) ((int)((x).size()))
#define R(f) freopen(f,"r",stdin);
#define W(f) freopen(f,"w",stdout);
#define TEST int num_cases; cin>>num_cases;for(int case_id=1;case_id <= num_cases;++case_id)

typedef long long ll;
typedef unsigned long long ull;

/** Main Code starts here :) **/

#define SUBMIT

int main(){
    #ifdef SUBMIT
    R("A-large.in");
    W("Z.txt");
    #endif

    #ifdef SAMPLE
    R("example_input.txt");
    #endif

    TEST{
        int r,c,w;
        si(r);  si(c);  si(w);
        int ans = (c/w)*r + w-1 + (c%w==0 ? 0: 1);
        //db("CASE ",case_id);
        printf("Case #%d: %d\n",case_id, ans);


    }
}
