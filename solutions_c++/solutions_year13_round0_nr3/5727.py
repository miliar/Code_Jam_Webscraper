#include<cstdio>
#include<vector>
#include<cmath>
#include<string>
#include<cstring>
#include<algorithm>
#include<queue>
#include<set>
#include<stack>
#include<map>
#include<sstream>
#include<bitset>
#include<deque>
#include<utility>
#include<cstdlib>
#include<iomanip>
#include<cctype>
#include<climits>
#include<iostream>
using namespace std;
#define ll             long long
#define ull            unsigned long long
#define all(x)         x.begin(),x.end()
#define vi             vector<int>
#define vvi            vector<vector<int> >
#define INF            2147483647
#define LIMIT          1000
#define mod            1000000007
#define pi             pair<int,int>
#define mp             make_pair
#define pb(v)          v.push_back
#define sz(x)          x.size()
string tostr(ll x)     { stringstream ss; ss << x; return ss.str(); }
ll toint(string &s)    { stringstream ss; ss << s; long long x; ss >> x; return x; }
ll gcd(ll a,ll b){return b?gcd(b,a%b):a;}
int arr[1001][1001]={0};
int main()
{
    #ifndef ONLINE_JUDGE
     freopen("C-small-attempt0.in","r",stdin);
     freopen("output.txt","w",stdout);
    #endif
	 int ans=0;
			for(int j=1;j<=1000;j++)
			{
				int l=sqrt((double)j);
				if(l*l==j)
				{
					string s1=tostr(j);
					string s2=s1;
					reverse(all(s2));
					if(s1==s2)
					{
						s1=tostr(l);
						s2=s1;
						reverse(all(s2));
						if(s1==s2)ans++;
					}
				}
				arr[1][j]=ans;
			}
			
    int t;
	cin>>t;
	for(int test=1;test<=t;test++)
	{
		int a,b;
		cin>>a>>b;
		cout<<"Case #"<<test<<": "<<arr[1][b]-arr[1][a-1]<<endl;
	}
    return 0;
}