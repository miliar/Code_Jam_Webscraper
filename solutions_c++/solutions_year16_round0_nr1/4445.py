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

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int test;
	cin >> test;
	for(int cs=1;cs<=test;++cs)
	{
		ll n;
		cin >> n;
		if(n==0)
			cout << "Case #" << cs << ": " << "INSOMNIA" << endl;
		else{
		
		bool v[10] = {false};
		int cnt = 0;
		ll p=n;
		
		while(cnt<10)
		{
			ll tmp = p;
			while(tmp>0)
			{
				int ld = tmp%10;
				if(v[ld]==false)
				{
					v[ld]=true;
					cnt++;
				}
				tmp/=10;
			}
			if(cnt==10)
				break;
			p += n;
		}
		
		cout << "Case #" << cs << ": " << p << endl;
		}
	}

  	return 0;
}

