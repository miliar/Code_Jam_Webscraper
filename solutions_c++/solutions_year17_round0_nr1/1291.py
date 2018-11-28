#include<bits/stdc++.h>
using namespace std;
 
// Numeric Constants
#define MOD 1000000007
#define maxs 250005
#define mins 1005
#define eps 0.000000000001
#define imax 2000000200
#define llmax 1000000002000000000ll
 
// Others
#define ll long long int
#define pb push_back
#define gc getchar_unlocked
#define iosbase ios_base::sync_with_stdio(false)
#define pii pair<int,int>
#define pll pair<ll,ll>
#define ppi pair<pair<int,int>,int>
#define ppl pair<pll,ll>
#define vi vector<int>
#define sc scanf
#define pr printf
#define lld I64d
#define F first
#define S second
#define siter set<int>::iterator
#define p_pq priority_queue
#define ub upper_bound
#define lb lower_bound

ll cnt[1001];

int main()
{	
	ll t,n,k,fl,sum;
	scanf("%lld",&t);
	string s;
	for(ll o=1;o<=t;++o)
	{
		sum=0;
		cin>>s>>k;
		n=s.length();
		memset(cnt,0,sizeof cnt);
		for(ll i=0;i<=n-k;++i)
		{
			if((cnt[i]==0&&s[i]=='-')||(cnt[i]==1&&s[i]=='+'))
			{
				sum++;
				for(ll j=i;j<i+k;++j)
					cnt[j]=(cnt[j]+1)%2;
			}

		}
		fl=1;
		for(ll i=0;i<n;++i)
		{
			if((cnt[i]==0&&s[i]=='-')||(cnt[i]==1&&s[i]=='+'))
			{
				fl=0;
				break;
			}
		}
		if(fl)
			printf("Case #%lld: %lld\n",o,sum);
		else
			printf("Case #%lld: IMPOSSIBLE\n",o);
	}
	return 0;
}