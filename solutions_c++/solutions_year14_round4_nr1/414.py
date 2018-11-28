#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

const int maxn=1e4+5;

int n,m,f[maxn],ans;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-ans.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++){
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++)
            scanf("%d",&f[i]);
        ans=n;
        sort(f,f+n);
        for(int i=0,j=n-1;i<j;i++){
            while(j>i&&f[i]+f[j]>m)j--;
            if(j>i&&f[i]+f[j]<=m){
                ans--;
                j--;
            }
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
