#define PROB ""
//#define SUBMIT

#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>

#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <list>


#pragma warning(disable:4996)
using namespace std;

#define EXIT exit(0);
#define INP(_X) scanf("%d",& _X);
#define OUT(_X) printf("%d ",_X);
#define abs(_Z) (((_Z)<0)?-(_Z):(_Z))

#define f0(_X,_Y) for((_X)=0;(_X)<(_Y);++(_X))
#define f1(_X,_Y) for((_X)=1;(_X)<=(_Y);++(_X))
#define ff(_X,_Y,_Z) for((_X)=(_Y);(_X)<=(_Z);++(_X))
#define fF(_X,_Y,_Z) for((_X)=(_Y);(_X)<(_Z);++(_X))

#define rf0(_X,_Y) for(_X=(_Y)-1;(_X)>=0;--(_X))
#define rf1(_X,_Y) for(_X=(_Y);(_X)>0;--(_X))
#define rff(_X,_Y,_Z) for(_X=(_Y);(_X)>=(_Z);--(_X))
#define rfF(_X,_Y,_Z) for(_X=(_Y);(_X)>(_Z);--(_X))

#define sz(_X) _X.size()
typedef long long ll;

#ifdef SUBMIT
    #define FIN
    #define FOUT
    #define LINE
    #define PRT(_X)
    #define DOUT(_X)
    #define DLINE
    #define TIME
#else
    #define FIN freopen("input" PROB ".txt","r",stdin);
    #define FOUT freopen("output" PROB ".txt","w",stdout);
    #define LINE printf("\n");
    #define PRT(_X) std::cout<< #_X ": "<<_X<<std::endl;
    #define DOUT(_X) fprintf(stderr,"%d ",_X);
    #define DLINE fprintf(stderr,"\n");
    #define TIME fprintf(stderr,"\n-----------\ntime : %.2f sec\n",double(clock())/CLOCKS_PER_SEC);
#endif

// struct XY
// {
//  int x,y;

//  XY(int _X=0,int _Y=0){x=_X;y=_Y;}
//  bool operator == (const XY &p) const{return x==p.x && y==p.y;}
//  bool operator < (const XY &p) const{if(x!=p.x) return x<p.x; return y<p.y;}
//  XY operator + (const XY &p) const{return XY(x+p.x,y+p.y);}
//  XY operator - (const XY &p) const{return XY(x-p.x,y-p.y);}
//  XY operator - () const{return XY(-x,-y);}
//  ll norm() const{return (ll)x*x+(ll)y*y;}
// };

// int ccw(const XY &p,const XY &q,const XY &r){ll _X=(ll)p.x*q.y+(ll)q.x*r.y+(ll)r.x*p.y-((ll)p.y*q.x+(ll)q.y*r.x+(ll)r.y*p.x); if(_X<0) return -1; return _X>0;}
//
// const int dx={1,0,-1,0};
// const int dy={0,1,0,-1};
//
// int k;
// f0(k,4)
// {
//  next.x = q[front].x + dx[k];
//  next.y = q[front].y + dy[k];
// }


int a[10002];
const int oo = 2e9;
int main()
{
    FIN FOUT

    int t,tc=0;
    int n;

    for(scanf("%d",&t);t--;)
    {
        int ans=0;
        scanf("%d",&n);
        for(int i=1;i<=n;++i) scanf("%d",&a[i]);
        for(int i=1;i<=n;++i)
        {
            int min=oo, k=0;
            for(int j=1;j<=n;++j)
                if(a[j]<min) min=a[j], k=j;

            int cnt1=0, cnt2=0;
            for(int j=1;j<k;++j) if(a[j]<oo) ++cnt1;
            for(int j=k+1;j<=n;++j) if(a[j]<oo) ++cnt2;
            ans += std::min(cnt1,cnt2);
            a[k]=oo;
        }
        printf("Case #%d: %d\n", ++tc,ans);
    }

    return 0;
}
