//<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< This is </the_brainFuck> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#include <cstring>
#include<string>
#include<sstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
#include <memory.h>
#include <cassert>
//#include<bits/stdc++.h>
#define     mem(x,y)   memset(x,y,sizeof(x))
#define     PB(x)      push_back(x)
#define     PP()      pop_back()
#define     SZ(a)      a.size()
#define     slen(a)    a.length();
#define     clen(a)     strlen(a)
#define     SQR(a)     (a*a)
#define     all(v)     v.begin(),v.end()
#define     fr(i,a,b)  for(i=a;i<=b;i++)
#define     rfr(i,a,b) for(i=a;i>=b;i--)
#define     sf  scanf
#define     pf  printf
#define     mkp make_pair
#define     fs  first
#define     sd  second
#define     read(n)       scanf("%d",&n)
#define     read2(m,n)    scanf("%d %d",&m,&n)
#define     read3(m,n,p)  scanf("%d %d %d",&m,&n,&p)
#define     readl(n)      scanf("%I64d",&n);
#define     readl2(m,n)   scanf("%I64d %I64d",&m,&n)
#define     readl3(m,n,p) scanf("%I64d %I64d %I64d",&m,&n,&p)
#define     input freopen("ql.in","r",stdin);
#define     output freopen("ql.out","w",stdout);
//constants
#define     inf  1<<30
#define     sz   20002
#define     eps  1e-9
#define     mod  1000000007
#define     PI   2.0*acos(0.0)

using namespace std;

typedef long long ll;
typedef double dd;

int main(int argc, const char **argv)
{
    input;
    output;
    int tc,l,ncase=0,i;
    char in[1010];
    vector<char>out;
    vector<char>::iterator it;
    read(tc);
    while(tc--){
        sf("%s",in);
        l=strlen(in)-1;
        out.clear();
        out.PB(in[0]);
        fr(i,1,l){
            it=out.begin();
            if(in[i]>=*it)
                out.insert(it,in[i]);
            else
                out.PB(in[i]);
        }
        pf("Case #%d: ",++ncase);
        l=out.size()-1;
        fr(i,0,l)
            pf("%c",out[i]);
        pf("\n");
    }
    return 0;
}
