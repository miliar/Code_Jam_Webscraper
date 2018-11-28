//Author: Vineet Shah
//IIT Indore
#include<bits/stdc++.h>
#define rep(i,start,lim) for(long long i=start;i<lim;i++)
#define repd(i,start,lim) for(long long i=start;i>=lim;i--)
#define MOD 1000000007
#define scan(x) scanf("%lld",&x)
#define print(x) printf("%lld",x)
#define sz(a) int((a).size())
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define br printf("\n")
#define bit(x,i) (x&(1<<i))
using namespace std;
typedef long long lld;
lld sum=0,n;
bool check(vector<pair<lld,char> >& v)
{
	if(sum==0) return 0;
	sort(v.rbegin(),v.rend());
	lld count=0,count2=0;
	rep(i,0,n)
		if(v[i].first==(sum/2))
			count++;
		else if(v[i].first==0)	
			count2++;
	if(count==2 || count==0)
	{
		if(v[0].first>=1)
		{
			v[0].first--,sum--;	
			cout<<(char)(v[0].second+'A');
		}
		if(v[1].first>=1)
		{
			v[1].first--,sum--;	
			cout<<(char)(v[1].second+'A');
		}
		cout<<" ";
		return 1;
	}
	else 
	{
		if(v[0].first>=1)
		{
			v[0].first--,sum--;	
			cout<<(char)(v[0].second+'A');
		}
		if(v[0].first>=1)
		{
			v[0].first--,sum--;	
			cout<<(char)(v[0].second+'A');
		}
		cout<<" ";
		return 1;
	}
	
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);	
	lld t,x;
	cin>>t;
	rep(ttt,1,t+1)
	{
		cin>>n,sum=0;
		vector<pair<lld,char> > v;
		rep(i,0,n)
		{
			cin>>x;
			sum+=x;
			v.pb(mp(x,i));
		}
		printf("Case #%lld: ",ttt);
		while(check(v)) ;
		br;
	}
	return 0;
}


