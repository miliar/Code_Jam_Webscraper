#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <algorithm>

using namespace std;

const int maxn=1e3+5;

int n,m,f[maxn],g[maxn];
map<int,int> S;
int tree[maxn];

void add(int x){
    while(x<=n){
        tree[x]++;
        x+=x&(-x);
    }
}

int back(int x){
    int ans=0;
    while(x>0){
        ans+=tree[x];
        x-=x&(-x);
    }
    return ans;
}

void myswap(int a,int b){
    swap(f[a],f[b]);
    g[f[a]]=a;
    g[f[b]]=b;
}

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-ans.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++){
        scanf("%d",&n);
        S.clear();
        for(int i=0;i<n;i++){
            scanf("%d",&f[i]);
            g[i]=f[i];
        }
        sort(g,g+n);
        for(int i=0;i<n;i++)
            S[g[i]]=i;
        for(int i=0;i<n;i++)
            f[i]=S[f[i]];
        int l=0,r=0,ans=0;
        for(int i=0;i<n;i++)
            g[f[i]]=i;
        for(int i=0;i<n;i++){
            if(g[i]-l<n-r-g[i]-1){
                //printf("%d->%d\n",g[i],l);
                while(g[i]!=l){
                    myswap(g[i],g[i]-1);
                    //printf("%d\n",g[i]);
                    ans++;
                }
                l++;
            }
            else{
               // printf("%d->%d\n",g[i],n-r-1);
                while(g[i]!=n-r-1){
                    myswap(g[i],g[i]+1);
                    //printf("%d\n",g[i]);
                    ans++;
                }
                r++;
            }
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
