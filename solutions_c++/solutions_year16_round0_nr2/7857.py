#include <bits/stdc++.h>
using namespace std;
#define ReadFile freopen("I:/CODE/B-large.in","r",stdin)
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

int main()
{
	ReadFile;
	Boost;
	int t;
	cin>>t;
	int flips=0;
	int len;
	string inp,st;
	bool beg=0;//0-plus,1-minu
	for(int l=1;l<=t;l++)
	{
		cin>>inp;
		len=inp.size();
		flips=0;
		beg=(inp[0]=='-');
		cout<<"Case #"<<l<<": ";
		for(int i=1;i<len;i++)
		{
			if(inp[i]!=inp[i-1])flips++;
		}
		if(flips==0)
		{
			if(!beg)cout<<0<<endl;
			else cout<<1<<endl;
		}
		else
		{
			len=flips+1;
			if(!beg)
			{
				cout<<2*(len/2)<<endl;
			}
			else
			{
				len--;
				cout<<1+2*(len/2)<<endl;
			}
		}
	}

	return 0;
}

