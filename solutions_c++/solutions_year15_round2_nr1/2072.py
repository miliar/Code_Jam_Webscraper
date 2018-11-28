#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<fstream>
#include<cstring>
#include<stack>
#include<cstdio>
#include<cmath>
#include<set>
#include<map>
#include<queue>
#define ll long long int
using namespace std;
ll reverse(ll n)
{
   ll a,ans=0;
   while(n!=0)
   {
       a=n%10;
       ans=ans*10;
       ans+=a;
       n/=10;
   }
   return ans;
}
ll dp[1000005];
int main()
{
	ifstream cin;
	ofstream cout;
	cin.open("C:\\Users\\Admin\\Downloads\\12.in");
	cout.open("C:\\Users\\Admin\\Downloads\\out.txt");
   int t,i,x=1;
   cin>>t;
   ll n;
   dp[0]=0;
   for(i=1;i<=11;i++)
        dp[i]=dp[i-1]+1;
   for(i=12;i<1000001;i++)
   {
                ll x=reverse(i);
                if(x!=i && dp[x]!=0 && i%10!=0)
                        dp[i]=min(dp[i-1]+1,dp[x]+1);
                else
                   dp[i]=dp[i-1]+1;
   }
  
  while(t--)
   {
       cin>>n;
       cout<<"Case #"<<x++<<": "<<dp[n]<<endl;
   }
   return 0;
}