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

int dp[1005][15];
int v[15];
int r;
int n;
int e0;

int solve(int e,int x){
    if(x==n) return dp[e][x]=0;
    //cout<<e<<" "<<x<<endl;
    if(dp[e][x]==-1){
        dp[e][x]=0;
        for(int i=0;i<=e;i++)
            dp[e][x]=max(dp[e][x],i*v[x]+solve(min(e-i+r,e0),x+1));
    }

    return dp[e][x];
}

int main(){
    int test;
    scanf("%d",&test);
    
    for(int tt=1;tt<=test;tt++){      
        printf("Case #%d: ",tt);
        scanf("%d %d %d",&e0,&r,&n);
        for(int i=0;i<n;i++) scanf("%d",&v[i]);
        memset(dp,-1,sizeof(dp));
        printf("%d",solve(e0,0));       
        printf("\n");
    }

    return 0;
}
