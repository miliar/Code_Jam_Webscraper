#include<bits/stdc++.h>

#define repi(n) for(int i=0;i<(n);++i)
#define repj(n) for(int j=0;j<(n);++j)
#define repr(i,m,n) for(int i=(m);i<=(n);++i)
#define rep1i(n) for(int i=1;i<=(n);++i)
#define sz(a) int((a).size)
#define pb(v) push_back(v)
#define mp(a,b)	make_pair((a),(b))
#define all(v) (v).begin(),(v).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i!=(c).end();++i)
#define pre(c,v) ((c).find()!=(c).end)
#define vpre(c,v) (find(all(c))!=(c).end())
#define nl cout<<endl

#define fi first
#define sec second

using namespace std;

typedef long long int ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vii;
typedef vector<vl> vll;
typedef pair<int,int> ii;

void mod(int i,int j,string& a)
{
	reverse(a.begin(),a.begin()+(j-i+1));
	for(int k=i;k<=j;++k)
	{
		if(a[k]=='+')
			a[k]='-';
		else
			a[k]='+';
	}
}

ll op(int i,int j,string& a)
{
	if(a[j]=='+')
		return 0;
	
	if(a[i]=='-')
	{
		mod(i,j,a);
		return 1;
	}
	
	if(a[i]=='+')
	{
		int k=j-1;
		while(k>0 && a[k]=='-')
			--k;
		mod(i,k,a);
		return 1;
	}
	
}

ll solve(string& a)
{
	ll ans = 0;
	int i=0, j= a.size()-1;
	
	while(j>=0)
	{
		while(a[j]=='+')
			--j;
		if(j>=i)
			ans += op(i,j,a);
		else
			break;
	}
	
	return ans;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int test;
	cin >> test;
	for(int cs=1;cs<=test;++cs)
	{
		ll ans = 0;
		string s;
		cin >> s;
		
		ans = solve(s);
		
		cout << "Case #" << cs << ": " << ans << endl;
	}



  	return 0;
}

