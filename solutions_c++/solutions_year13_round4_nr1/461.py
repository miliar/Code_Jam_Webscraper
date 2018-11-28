#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;

typedef long long LL;

const int INF = 1000002013;

int n,m,cnt[2005];
vector<int> u;

int locate(int x, const vector<int>& u){
    return lower_bound(u.begin(),u.end(),x)-u.begin();
}

int gao(int x, int y){
    int low=INF,ret=0;
    for(int i=x;i<=y;i++){
        if(!cnt[i]){
            if(low==INF) continue;
            int l=u[i]-u[x];
            int w=(n+(n-l+1ll))*l/2%INF;
            for(int j=x;j<i;j++) cnt[j]-=low;
            ret=(ret+w*LL(low)+gao(x,i))%INF;
            low=INF;
        }else{
            if(low==INF) x=i;
            low=min(low,cnt[i]);
        }
    }
    return ret;
}

int main(){
    int cs,no=0;
    scanf("%d",&cs);
    while(cs--){
        int sum=0,x[1005],y[1005],c[1005];
        u.clear();
        memset(cnt,0,sizeof(cnt));
        scanf("%d%d",&n,&m);
        for(int i=0;i<m;i++){
            scanf("%d%d%d",x+i,y+i,c+i);
            u.push_back(x[i]);
            u.push_back(y[i]);
            int l=y[i]-x[i];
            int w=(n+(n-l+1ll))*l/2%INF;
            sum=(sum+w*LL(c[i]))%INF;
        }
        sort(u.begin(),u.end());
        u.erase(unique(u.begin(),u.end()),u.end());
        for(int i=0;i<m;i++){
            x[i]=locate(x[i],u);
            y[i]=locate(y[i],u);
            for(int k=x[i];k<y[i];k++) cnt[k]=(cnt[k]+c[i])%INF;
        }
        int ans=gao(0,u.size());
        printf("Case #%d: %d\n",++no,(sum-ans+INF)%INF);
    }
}
