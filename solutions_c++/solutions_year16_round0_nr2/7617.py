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
#define     input freopen("qbl.in","r",stdin);
#define     output freopen("qbl.out","w",stdout);
//constants
#define     inf  1<<25
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
    int tc,ncase=0,i,ind,l,ans,cnt;
    string in,temp;
    cin>>tc;
    while(tc--){
        cin>>in;
        l=in.length()-1;
        ans=0;
        while(1){
            cnt=0;
            fr(i,0,l){
                if(in[i]=='-')
                    cnt++;
            }
            if(!cnt)
                break;
            i=0;
            if(in[0]=='+'){
                while(in[i]=='+'){
                    in[i]='-';
                    i++;
                }
            }
            else{
                fr(i,0,l){
                    if(in[i]=='-')
                        ind=i;
                }
                temp="";
                rfr(i,ind,0){
                    if(in[i]=='+')
                        temp+='-';
                    else
                        temp+='+';
                }
                fr(i,0,ind)
                    in[i]=temp[i];
            }
            ans++;
        }
        cout << "Case #" << ++ncase << ":" << " " << ans << endl;
    }
    return 0;
}
