#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<string>
#include<queue>
#include<set>
#include<map>
#include<iostream>
#include<cmath>
using namespace std;
#define mem(a,b) memset(a,b,sizeof(a))
#define pb push_back
typedef long long ll;

const int N = 1100;

double a[N],b[N];
int n;

int dp[N][N];
int dfs(int i,int j) {
    if(i==n) return 0;
    int &ans=dp[i][j];
    if(~ans) return ans;
    if(a[i]<b[j]) ans=dfs(i+1,j);
    else {
        if(a[i]>b[j+n-1-i]) ans=n-i;
        else ans=max(dfs(i+1,j), 1+dfs(i+1,j+1));
    }
    return ans;
}
int dwar() {
    mem(dp,-1);
    return dfs(0,0);
}

int vis[N];
int war() {
    int ret=0;
    mem(vis,0);
    for(int i=0;i<n;i++) {
        for(int j=0;j<n;j++) if(!vis[j]) {
            if(b[j]>a[i]) {
                ret++;
                vis[j]=1;
                break;
            }
        }
    }
    return n-ret;
}

int main()
{
	int T; scanf("%d",&T);
	for(int ka=1;ka<=T;ka++) {
        scanf("%d",&n);
        for(int i=0;i<n;i++) scanf("%lf",&a[i]);
        for(int i=0;i<n;i++) scanf("%lf",&b[i]);
        sort(a,a+n);
        sort(b,b+n);
        printf("Case #%d: %d %d\n",ka,dwar(),war());
	}

    return 0;
}
