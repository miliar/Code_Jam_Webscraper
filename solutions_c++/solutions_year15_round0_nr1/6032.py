#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define mod 1000000007

using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef vector< vector<int> > VVI;
typedef pair< int, int > PII;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int t,Case=0;
	cin>>t;
	while(t--)
	{
		Case++;
		string s;
		int n,ans=0,cnt=0; cin>>n>>s;
		for(int i=0; i<=n; i++)
		{
			if(cnt<i && (s[i]-'0')>0)
			{
				ans += (i-cnt);
				cnt=i;
			}
			cnt += s[i]-'0';
		}
		cout<<"Case #"<<Case<<": "<<ans<<"\n";
	}
	return 0;
}
