#include<cstdio>
#include<cstring>
#include<bitset>
#include<stack>
#include<queue>
#include<vector>
#include<algorithm>
#include<set>
#include<cmath>
#include<map>
#include<stack>
#include<queue>
#include<cassert>
#define N 111111
#define M 555555
#define LL long long
#define FOE(i,a,b) for(int i=(a);i<=(b);++i)
#define FOD(i,a,b) for(int i=(b);i>=(a);--i)
#define CLR(a,b) memset(a,b,sizeof(a))
#define lc(x) (x<<1)
#define rc(x) (lc(x)|1)
using namespace std;
int t,cs=0,x,r,c,n,m,q,k,ans;
int a[N],b[N];
int main(){
    scanf("%d",&t);
    while(t--){
        bool rw=0;
        scanf("%d%d%d",&x,&r,&c);
        if(x>=7)rw=1;
        else if(x>max(r,c))rw=1;
        else if((r*c)%x)rw=1;
        int gg=(x+1)/2;
        if(x>=3 && (r<=gg || c<=gg))rw=1;
        ++cs;
        if(x==3 && min(r,c)==2 && max(r,c)==3)rw=0;
        //printf("x:%d r:%d c:%d ",x,r,c);
        if(rw)printf("Case #%d: RICHARD\n",cs);
        else printf("Case #%d: GABRIEL\n",cs);

    }
	return 0;
}

