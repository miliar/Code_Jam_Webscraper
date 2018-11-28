#include <cstdio>
#include <iostream>
#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <functional>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef map<int,int> mii;
typedef vector<int> vi;
typedef vector< vector<int> > vvi;
typedef vector<char> vc;
typedef vector<bool> vb;
typedef vector<string> vs;

#define rep(i,n) for(int i=0;i<n;i++)
#define forup(i,a,b) for(int i=a;i<=b;i++)
#define fordn(i,a,b) for(int i=a;i>=b;i--)
#define drep(i,n) for(i=0;i<n;i++)
#define dforup(i,a,b) for(i=a;i<=b;i++)
#define dfordn(i,a,b) for(i=a;i>=b;i--)
#define all(x) x.begin(),x.end()
#define permute(x) next_permutation(all(x))
#define ri(x) scanf("%d",&x)
#define rl(x) scanf("%lld",&x)
#define rd(x) scanf("%lf",&x);
#define rs(x) scanf(" %s",x);
#define pb push_back
#define mp make_pair
#define fi first
#define sc second
#define MOD 1000000007

string str1,str2;
int dp[103][103];
int solve(int i,int j){
	if(i==str1.size()-1 || j==str2.size()-1)
		if(i==str1.size()-1 && j==str2.size()-1)
			return 0;
		else{
			if(i==str1.size()-1)
			{
				int c=0;
				while(str2[j]==str2[j-1])
				{
					j++;
					c++;
				}
				if(str2[j]=='0')
					return c;
				else
					return 500;
			}
			else
			{
				int c=0;
				while(str1[i]==str1[i-1]){
					i++;
					c++;
				}
				if(str1[i]=='0')
					return c;
				else
					return 500;

			}

		}
		
	if(dp[i][j]!=-1)
		return dp[i][j];
	int m=500;
	if(str1[i]==str2[j])
		m=min(m,solve(i+1,j+1));
	else
	{
		if(str1[i-1]==str1[i] )
			m=min(m,1+solve(i+1,j));
		if(str2[j-1]==str2[j] )
			m=min(m,1+solve(i,j+1));
		if( str1[i-1]==str2[j])
			m=min(m,1+solve(i,j+1));
		if( str1[i]==str2[j-1])
			m=min(m,1+solve(i+1,j));
	}
	return dp[i][j]=m;

}
int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int n,t;
	cin>>t;
	for(int k=1;k<=t;k++){
		cin>>n;
		memset(dp,-1,sizeof dp);
		cin>>str1>>str2;
		str1='0'+str1+'0';
		str2='0'+str2+'0';
		printf("Case #%d: ",k);
		int ans=solve(0,0);
		if(ans<500)
			printf("%d\n",ans);
		else
			printf("Fegla Won\n");
	}
	return 0;
}


