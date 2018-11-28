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
#define MAX 100000001

using namespace std;

typedef long long int ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vii;
typedef vector<vl> vll;
typedef pair<int,int> ii;

bool v[MAX];
ll sp[MAX];
vl pr;

void Sieve(){
	pr.pb(2);
	for (ll i = 2; i < MAX; i += 2)	sp[i] = 2;
	for (ll i = 3; i < MAX; i += 2){
		if (!v[i]){
			sp[i] = i;
			pr.pb(i);
			for (ll j = i; (j*i) < MAX; j += 2){
				if (!v[j*i])	{
				v[j*i] = true; sp[j*i] = i;
				}
			}
		}
	}
}

ll po(ll base, ll exp)
{
	if(exp==0)
		return 1;
	ll tmp = po(base,exp/2);
	if(exp%2)
		return tmp*tmp*base;
	return tmp*tmp;
}

int main()
{
	freopen("out.txt","w",stdout);
/*
	int test;
	cin >> test;
	for(int cs=1;cs<=test;++cs)
	{


	}
*/
	Sieve();
//	cout << "Sieve done\n\n";
	cout << "Case #1:\n";	
	int anscnt = 0;

	for(int i=(1<<15)+1;i<(1<<16);i+=2)
	{
		string a = "";
		int tmp = i;
		while(tmp>0)
		{
			if(tmp%2)
				a += "1";
			else a+= "0";	
			tmp/=2;
		}
//		reverse(all(a));
//		cout << a << endl;

		vi ans;
		for(int j=2;j<=10;++j)
		{
			ll x=0;
			for(int k=0;k<a.size();++k)
			{
				if(a[k]=='1')
					x += po(j,k);	
			}
//			cout <<"\n" <<j <<" " << x << " ";

//		cout <<endl;
			if(x<=100000000)
			{
				if(sp[x]==x)
					break;
				else
				{
					ans.pb(sp[x]);
				}
			}
			else if(x<=10000000000000000)
			{
				int k;
				for(k=0;k<pr.size() && pr[k]<=(ll)sqrt(x);++k)
				{
					if(x%pr[k]==0)
					{
						ans.pb(pr[k]);
						break;
					}
				}
				if(k==pr.size())
					break;
			}
			else
			{
				cout << "Out of Range :( :(\n";
			}
		}
		if(ans.size()==9)
		{
			++anscnt;
			reverse(all(a));
//			cout << i << " ";
			cout << a << " ";
			repj(ans.size())
				cout << ans[j] << " ";
			cout << "\n";
		}
		if(anscnt>=50)
			break;
	}

  	return 0;
}

