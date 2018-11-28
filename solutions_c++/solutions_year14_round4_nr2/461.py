#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int maxn = 1005;

int n;

struct node{
    int num,id;
}poi[maxn];

bool cmp(const node &a,const node &b){
    return a.num<b.num;
}

int sum[maxn];

void init(){
    memset(sum,0,sizeof(sum));
}

inline int Lowbit(int x){
    return x&(-x);
}

void add(int x,int y){
    for(;x<=n;x+=Lowbit(x))sum[x]+=y;
}

int calsum(int x){
    int res=0;
    for(;x>0;x-=Lowbit(x))res+=sum[x];
    return res;
}

int solve(){
    int ans=0,cnt=n,tem;
    for(int i=0;i<n;i++){
        tem=calsum(poi[i].id);
        tem=poi[i].id-tem-1;
        if(tem<cnt-1-tem)ans+=tem;
        else ans+=cnt-1-tem;
        add(poi[i].id,1);
        cnt--;
    }
    return ans;
}

int main(){
    int i,j,k;
    int L,T;
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    for(L=1;L<=T;L++){
        scanf("%d",&n);
        for(i=0;i<n;i++){
            scanf("%d",&poi[i].num);
            poi[i].id=i+1;
        }
        sort(poi,poi+n,cmp);
        init();
        printf("Case #%d: %d\n",L,solve());
    }
    return 0;
}
