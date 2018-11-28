#include <cstdio>
#include <iostream>
#include <bits/stdc++.h>

using namespace std;
/*
# # define mod 1000000007
# vector<pair<int,long long > > p[100003];
# long long  dp[100003],ans;
# void dfs(int n,int par)
# {
#     int i;
#     long long sum=0;
#     for(i=0;i<p[n].size();i++)
#     {
#         long long w=p[n][i].second;
#         int node=p[n][i].first;
#         //cout<<i;
#         if(p[n][i].first!=par)
#         {
#             dfs(p[n][i].first,n);
#         dp[n]=(dp[n]+(w*(dp[node]+1))%mod)%mod;
#         }
# 
#     }
#     ans=(ans+dp[n])%mod;
#     sum=dp[n];
#     //cout<<ans<<endl;
#     for(i=0;i<p[n].size();i++)
#     {
#         long long w=p[n][i].second;
#         int node=p[n][i].first;
#         if(p[n][i].first!=par){
#         sum=(sum+mod-(w*(dp[node]+1))%mod)%mod;
#         ans=(ans+(sum*(w*(dp[node]+1))%mod)%mod)%mod;}
#     }
#    //8 cout<<n<<' '<<ans<<endl;
# }
# int main()
# {
#     int n,i,u,v;
#     long long w;
#     scanf("%d",&n);
#     for(i=0;i<n-1;i++)
#     {
#         scanf("%d%d%lld",&u,&v,&w);
#         p[u].push_back(make_pair(v,w));
#         p[v].push_back(make_pair(u,w));
#     }
#    // cout<<p[1].size();
#     dfs(1,0);
#     printf("%lld",ans);
#     return 0;
# }
*/
int a = 2;
int foo(){
	int a;
	cout<<a;
}

int main() {
	foo();
	cout<<a;
	return 0;
}
