#include<cstdio>
#include<iostream>
#include<cmath>
#include<algorithm>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<vector>
#include<map>
#include<stack>
#include<string>

using namespace std;

const int INF=2000000000;

int T;
int n;
int a[1007];

int solve(int lim){
    int ans=lim;
    for (int i=0;i<n;i++){
            ans+=(a[i]/lim-1);
            if (a[i]%lim!=0) ans++;
    }
    return ans;
}

int main(){
    freopen("B-large.in","r",stdin);
    freopen("output.out","w",stdout);
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++){
            scanf("%d",&n);
            int MAX=0;
            int ans=INF;
            for (int i=0;i<n;i++){
                    scanf("%d",&a[i]);
                    MAX=max(MAX,a[i]);
            }
            for (int i=MAX;i>=1;i--){
                    int tmp=solve(i);
             //       printf("cas %d i %d solve(i) %d\n",cas,i,tmp);
                    if (ans>tmp) ans=tmp;
            }
            printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
/*
3
1
3
4
1 2 1 2
1
4
*/
