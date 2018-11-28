#include<bits/stdc++.h>
using namespace std;
#define FOR(i,a,b) for(int i=a;i<b;++i)
#define FORC(i,a,b) for(int i=a;i<=b;++i)
#define FORD(i,a,b) for(int i=a;i>b;--i)
#define ini(arr,val) memset(arr,val,sizeof(arr))
#define pii pair<int,int>
#define vi vector<int>
#define f first
#define s second
#define si set<int>
#define pb push_back
#define deb(d,a,b) for(d=a;d<b;++b)
#define p(val) printf("%d ",val)
#define pe(val) printf("%d\n",val)
#define qt queue<int>
#define size(arr) arr.size()
#define pc(s) printf("%c ",s)
#define pce(s) printf("%c\n",s);
#define ll  long long int
#define jam(x,y) printf("Case #%d: %d",x+1,y);
#define ld long double
int main()
{
   int t;
   cin >> t;
   FOR(it,0,t)
   {
      long double c,f,x;
      cin >> c >> f >> x;
      int count = x/f + 10000;
      long double dp[count];//ei
      
      dp[0] = c/2;//p
      FOR(i,1,count)
         dp[i] = dp[i-1] + (c/(2+(i*f))) ;
      
      long double mini = x*0.5;
      FOR(i,1,count)
         mini = min(mini,dp[i-1]+(x/(2+(i*f))));
      
      printf("Case #%d: %.7llf\n",it+1,mini);//o
   }
   
}  
 
         
      
      
      
      
      
