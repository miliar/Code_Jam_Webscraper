#include <bits/stdc++.h>
using namespace std;
#define ReadFile freopen("I:/CODE/A-large.in","r",stdin)
#define Boost ios_base::sync_with_stdio(false)
#define setP(s,p) fixed<<setprecision(p)<<ssss
#define pb emplace_back
#define MOD 1000000007
#define MAX 100010
#define INF LONG_MAX
#define f first
#define s second
#define endl '\n'

typedef long long int ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

vector<int> num;
vector<int> org;
set<int> used;
int m;
void initialize()
{
	num.clear();
	used.clear();
	org.clear();
	m=2;
}
int main()
{
	ReadFile;
	Boost;
	int t;
	int n;
	int cp;
	int val=0;
	int carry=0;
	int sz;
	cin>>t;
	for(int loop=1;loop<=t;loop++)
	{
		cin>>n;
		cout<<"Case #"<<loop<<": ";
		if(n==0)
		{
			cout<<"INSOMNIA"<<endl;
			continue;
		}
		initialize();
		cp=n;
		while(cp>0)
		{
			num.pb(cp%10);
			org.pb(cp%10);
			used.insert(cp%10);
			cp/=10;
		}
		while(used.size()<10)
		{
			carry=0;
			sz=org.size();
			int ind=0;
			for(int i=0;i<sz;i++)
			{
				val=(num[i]+org[i]) + carry;
				num[i]=val%10;
				used.insert(num[i]);
				carry=val/10;
				//cout<<val<<" "<<carry<<endl; 
				ind++;
			}
			sz=num.size();
			while(carry>0)
			{
				if(ind<sz)
				{
					val=num[ind]+carry;
					num[ind]=val%10;
					used.insert(num[ind]);
					val/=10;
					carry=val;
				}
				else
				{
					num.pb(carry%10);
					used.insert(carry%10);
					carry/=10;
				}
			}
		}
		sz=num.size();
		for(int i=sz-1;i>=0;i--)cout<<num[i];
		cout<<endl;
	}


	return 0;
}

