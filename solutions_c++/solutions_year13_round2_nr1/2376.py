#include <string> 
#include <vector> 
#include <map> 
#include <utility> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <queue> 
#include <stack> 
#include <set> 
#include <sstream> 
#include <algorithm> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
using namespace std; 
  
#define INF 0x3f3f3f3f
#define ALL(v) v.begin(),v.end() 
typedef pair<char,int> pci;
typedef long long ll;
int arr[105],n;

int dp[10005][105];

int solve(int t,int x){
    
    if(x>=n) dp[t][x]=0;
    if(dp[t][x]==-1){
        dp[t][x]=0;
        if(t>arr[x])
            dp[t][x]=solve(t+arr[x],x+1);
        else{
            if(t+t-1>arr[x])
                dp[t][x]=1+solve(t+t-1+arr[x],x+1);
            else{
                dp[t][x]=1+min(solve(t+t-1,x),solve(t,x+1));            
            }
        }
    }
    //cout<<"--> "<<t<<" "<<x<<" "<<dp[t][x]<<endl;
    return dp[t][x];
}

int main(){
    int test;
    scanf("%d",&test);
        
    for(int tt=1;tt<=test;tt++){
        printf("Case #%d: ",tt);
        int a;
        scanf("%d %d",&a,&n);
        for(int i=0;i<n;i++)
            scanf("%d",&arr[i]);
        sort(arr,arr+n);
        memset(dp,-1,sizeof(dp));
        int res;
        if(a==1) res=n;
        else res=solve(a,0);
        printf("%d",res);
        printf("\n");
    }

    return 0;
}
