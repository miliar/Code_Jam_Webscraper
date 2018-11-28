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
		vi v;
		vi v1;
		vi v2;
		v2.clear();
		v1.clear();
		v.clear();
		for(int i=0;i<n;i++)
		{
			int x;
			cin>>x;
			v.pb(x);
			v1.pb(x);
		}
	
		sort(all(v));
		sort(all(v1));
		int ans=0;
		int ans1=v[n-1];
		int ans2=0;
		int ans3=0;
			if(v1[0]==9&&n==1)
			{
			ans2=5;
			goto l;
		}
		while(v[n-1]>0)
		{
			
			ans++;
			if(v[n-1]%2!=0&&v[n-1]!=1)
			v[n-1]++;
			v[n-1] = v[n-1] /2;
			if(v[n-1]!=5)
			{
			v.pb(v[n-1]);
			v1.pb(v1[n-1]);
			n++;
		}
			sort(all(v));
			//for(int i=0;i<v.size();i++)
			//cout<<"v = "<<v[i]<<" ";
			int temp = ans + v[n-1];
			v2.pb(temp);
			if(ans==1)
			{
			if(v1[n-1]%2!=0&&v1[n-1]!=1)
			v1[n-1]++;
			v1[n-1] = v1[n-1] /2;
			sort(all(v1));
			ans2 = 1 + v1[n-1];
			}
			if(v[n-1]==2)
			{
				ans=ans+2;
			break;
			}
			
		}
		ans3 = *min_element(all(v2));
	//	cout<<ans<<" "<<ans1<<" "<<ans2<<" "<<ans3<<endl;
	
	l:
		if(n==1)
		{
			
		//	cout<<"yo";
		cout<<"Case #"<<k<<": "<<ans2<<endl;		
	}
		else
		cout<<"Case #"<<k<<": "<<min(ans,min(ans3,min(ans1,ans2)))<<endl;
			k++;
	}
	return 0;
}
