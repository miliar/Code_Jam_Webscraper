#include <bits/stdc++.h>
#define pb push_back
#define sqr(x) (x)*(x)
#define sz(a) int(a.size())
#define reset(a,b) memset(a,b,sizeof(a))
#define oo 1000000007

using namespace std;

typedef pair<int,int> pii;
typedef long long ll;

const int maxn=1007;

int x[maxn],y[maxn],z[maxn],vx[maxn],vy[maxn],vz[maxn];
int T,n,s;
bool free1[maxn];

double dis(int i, int j){
    return sqrt(sqr(x[i]-x[j])+sqr(y[i]-y[j])+sqr(z[i]-z[j]));
}

int myq[maxn],first,last;

bool check(double len){
    myq[first=last=1]=1;
    for(int i=1; i<=n; ++i) free1[i]=1;
    free1[1]=0;
    while(first<=last){
        int u=myq[first++];
        for(int v=1; v<=n; ++v) if(free1[v] && dis(u,v)-1e-9<len){
            free1[v]=0;
            myq[++last]=v;
        }
    }
    return !free1[2];
}
int main(){
//    freopen("input.txt","r",stdin);
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);
    scanf("%d",&T);
    for(int tt=1; tt<=T; ++tt){
        scanf("%d%d",&n,&s);
        for(int i=1; i<=n; ++i) scanf("%d%d%d%d%d%d",x+i,y+i,z+i,vx+i,vy+i,vz+i);
        double left=0, right=oo, mid;
        for(int i=0; i<60; ++i){
            mid=(left+right)/2;
            if(check(mid)){
                right = mid;
            }else{
                left = mid;
            }
        }
        printf("Case #%d: %0.9f\n",tt,right);
    }
}

