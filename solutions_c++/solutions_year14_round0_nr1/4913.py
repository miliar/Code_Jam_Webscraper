#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<climits>
#include<cctype>
#include<iostream>
#include<algorithm>
#include<queue>
#include<vector>
#include<map>
#include<string>
#include<set>
#include<stack>
#define ll long long
#define MAX 1000
#define INF INT_MAX
#define eps 1e-6
#define REP(i,n) for (int i=0; i<n; i++)
#define FOR(i,s,t) for (int i=(s); i<=(t); i++)

using namespace std;


int main(){
    int vis[20],T,n;
    FILE *fp = fopen("out.txt", "w");
    scanf("%d",&T);
    for (int cas = 1; cas<=T; cas++){
        memset(vis,0,sizeof(vis));
        scanf("%d",&n);
        int t;
        for (int i=0; i<4; i++)
            for (int j=0; j<4; j++){
                scanf("%d",&t);
                if (i==n-1)
                    vis[t] = 1;
            }
        int cnt = 0,ans;
        scanf("%d",&n);
        for (int i=0; i<4; i++)
            for (int j=0; j<4; j++){
                scanf("%d",&t);
                if (i==n-1 && vis[t]){
                    cnt++;
                    ans = t;
                }
            }
        if (!cnt) fprintf(fp,"Case #%d: Volunteer cheated!\n",cas);
        else if (cnt==1) fprintf(fp,"Case #%d: %d\n",cas,ans);
        else fprintf(fp,"Case #%d: Bad magician!\n",cas);
    }
    return 0;
}
