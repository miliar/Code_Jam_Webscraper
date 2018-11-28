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
#include <bitset>
#include <numeric>
#include <cstring>
//#include <deque>
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

int main() 
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	int k = 1;
	while(t-->0)
	{
		int n;
		cin>>n;
		string s;
		cin>>s;
		int m = s.size();
		int sum[m+1],ans=0;
		sum[0]=0;
		sum[1]=s[0]-'0';
		for(int i=1;i<m;i++)
		{
			if(i>sum[i]&&s[i]!='0')
			{
				ans = ans + ((i)-sum[i]);
				sum[i+1] = sum[i] + (s[i]-'0') + ans; 
			}
			else
			{
				sum[i+1] = sum[i] + (s[i]-'0');
			}
			//cout<<sum[i+1]<<endl;
		}
			cout<<"Case #"<<k<<": "<<ans<<endl;
			k++;
	}
	return 0;
}
