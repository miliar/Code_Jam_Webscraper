/// BIS-MILLAHIR RAHMANIR RAHIM

#include<algorithm>
#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<iostream>
#include<fstream>
#include<numeric>
#include<string>
#include<vector>
#include<cstring>
#include<map>
#include<iterator>
#include<deque>
#include<climits>

using namespace std;

#define I1(n) scanf("%d",&n)
#define ILL1(n) scanf("%lld",&n)
#define I2(n1,n2) scanf("%d%d",&n1,&n2)
#define ILL2(n1,n2) scanf("%lld%lld",&n1,&n2)
#define I3(n1,n2,n3) scanf("%d%d%d",&n1,&n2,&n3)
#define ILL3(n1,n2,n3) scanf("%lld%lld%lld",&n1,&n2,&n3)

#define F(i, a, b) for(  i = (a); i <= (b); i++ )
#define FR(i, a, b) for(  i = (a); i < (b); i++ )
#define FRR(i, a, b) for(  i = (a); i >b; i-- )
#define Fs(i, sz) for( size_t i = 0; i < sz.size (); i++ )
#define Fe(it, x) for(typeof (x.begin()) it = x.begin(); it != x.end (); it++)
#define Pr(x) for(typeof (x.begin()) it = x.begin(); it != x.end (); it++) cout << *it << " "; cout << endl;

#define all(a) a.begin(),a.end()
#define pb push_back
#define pi acos(-1.0)
#define MEM(a,val) memset(a,val,sizeof(a))
#define eps 1e-9
#define Max(a,b) (a>b?a:b)
#define Min(a,b) (a<b?a:b)
#define sz(a) ((int)(a).size())
#define IN  freopen("input.txt","r",stdin)
#define OUT freopen("output.txt","w",stdout)
#define CLR(n) n.clear()
#define SQR(n) (n*n)
#define LEFT (idx<<1)
#define RIGHT (LEFT+1)
#define PC printf("Case %d:",cas++);

template<typename T> T POW(T B,T P){ if(P==0) return 1; if(P&1) return B*POW(B,P-1);  else return SQR(POW(B,P/2));}

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    OUT;


    int tc,cas=1;
    int a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,cnt=0;
    int area,st,ed;

    I1(tc);

    while(tc--)
    {
        I2(r,t);
        st = r;
        ed = r+1;
        cnt  = 0;
        while(t)
        {
            area = ( SQR(ed) - SQR(st));
            if(area<=t)
            {
                cnt++;
                t-=area;
            }
            else{break;}
           st+=2;
           ed+=2;
        }

        printf("Case #%d: %d\n",cas++,cnt);

    }



    return 0;
}
