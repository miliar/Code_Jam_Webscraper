#include "stdio.h"
#include "math.h"
#include "vector"
using namespace std;
int solve(int i,int j);
vector<vector<int> > dp(101,vector<int>(101,-1));
int main(){
    freopen("D-small-attempt1.in","r",stdin);
    freopen("last problem smallxxx.txt","w",stdout);
    int t,n,k,s;
    scanf("%d",&t);
    for(int l=1;l<=t;l++){
        scanf("%d %d %d",&n,&k,&s);
        int x=solve(n,k);
        if(x>s) printf("Case #%d: IMPOSSIBLE\n",l);
        else{
            printf("Case #%d: ",l);
            long long temp=1;
            long long tempx=(long long)pow(n,k-1);
            for(int i=1;i<=s;i++){
                printf("%lld ",temp);
                temp+=tempx;
            }
            printf("\n");
        }
    }
}
int solve(int i,int j){
    if(i<=j) return 1;
    if(dp[i][j]!=-1) return dp[i][j];
    return dp[i][j]=1+solve(i-j,j);
}
