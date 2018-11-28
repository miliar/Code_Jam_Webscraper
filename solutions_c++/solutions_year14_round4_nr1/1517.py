#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<math.h>
#include<map>
#include<vector>
#include<string>
#include<set>
#include<queue>
#define MP(x,y) make_pair(x,y)
#define clr(x,y) memset(x,y,sizeof(x))
#define forn(i,n) for(int i=0;i<n;i++)
#define sqr(x) ((x)*(x))
#define MAX(a,b) if(a<b) a=b;
#define ll long long
using namespace std;

int n,m;
int a[10005];
bool flag[10005];

int main() {
    freopen("/home/zyc/Downloads/in","r",stdin);
    freopen("/home/zyc/Downloads/out","w",stdout);
//    freopen("/home/zyc/Documents/Code/cpp/in","r",stdin);
    int T,cas=0;
    scanf("%d",&T);
    while(T--){
        scanf("%d%d",&n,&m);
        clr(flag,0);
        for(int i=0;i<n;i++){
            scanf("%d",&a[i]);
        }
        sort(a,a+n);
        int ans=0;
        int j=n-1;
        for(int i=0;i<n;i++){
            while(j>i&&a[i]+a[j]>m) j--;
            if(j>i){
                flag[i]=flag[j]=1;
                ans++;
                j--;
            }else break;
        }
        for(int i=0;i<n;i++) if(!flag[i]) ans++;
        printf("Case #%d: %d\n",++cas,ans);
    }
    return 0;
}

