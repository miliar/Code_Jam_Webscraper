#include <stdio.h>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <stdlib.h>
#include <math.h>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
using namespace std;
#define ll long long 
#define _ ios::sync_with_stdio(false);
#define mem(x,a) memset(x,(a),(int)(sizeof(x)))
#define pii pair<int,int>
#define fr(i,a,n) for(int i=(a);i<=(n);i++)
#define frd(i,a,n) for(int i=(a);i>=(n);i--)
#define nl printf("\n")
#define pb push_back
#define mp make_pair 
#define F first 
#define V vector
#define upperlimit 5000009
ll mod=1e9+7;
V<string> m[20];
V<int> res;
bool prime[5000005];
V<ll> vv[11];
ll check(ll n)
{
	if(n%2==0)
		return 2LL;
	for(ll i=3LL;i<=sqrt(n);i++)
		if(n%i==0)return i;
	return n;
}
ll two[21],xx[12][20];
void sieve(int n)
{
	mem(prime,true);
	prime[0]=prime[1]=false;
	for(int i=4;i<=n;i+=2)prime[i]=false;
	for(int i=3;i*i<=n;i+=2)
	if(prime[i])
		for(int j=i*i;j<=n;j+= i*2)
			prime[j]=false;
	//for(int i=2;i<=50000;i++)if(prime[i])p.pb(i);
}
V<string> ans[20];
int rem=60;
void generate(string s)
{
	if(rem==0)return;
	if(s.size()>16)return;// try only find the first 100 numberss
	
	if(s.size()==15)
		{
			string t=s+'1';
			m[16].pb(t);
			int flag=1;
			for(int j=2;j<=10;j++)
			{
				ll val=0;
				for(ll r=15,x=0;r>=0;r--,x++)
				{
					if(t[r]=='1')val+=xx[j][x];
				}
				if(check(val)==val)flag=0;
			}
			if(flag)rem--,ans[16].pb(t);
		}
	generate(s+'0');
	generate(s+'1');
}
int main() {_
	fr(i,2,10)xx[i][0]=1;
	for(ll i=2LL;i<=10;i++)for(ll j=1;j<=16;j++)xx[i][j]=xx[i][j-1]*i*1LL;
	sieve(5000005);
	int t;
	cin>>t;
	//cout<<res.size()<<endl;
	m[2].pb("11");
	generate("1");
	//for(auto x:ans[16])cout<<x<<endl;
	
	for(int i=0;i<60;i++)
	{
		string s=ans[16][i];
		for(int j=2;j<=10;j++)
		{
			ll val=0;
			for(ll r=15,x=0;r>=0;r--,x++)
				if(s[r]=='1')val+=xx[j][x];
			vv[j].pb(val);
		}
	}
	cout<<"Case #1:\n";
	fr(i,0,49)
	{
		//if(i==16)continue;
		cout<<ans[16][i]<<" ";
		for(int j=2;j<=10;j++)cout<<check(vv[j][i])<<" ";
		nl;
	}
	return 0;
}
