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


string str(int i)
{
	if(i==0)
		return "0";
	if(i==1)
		return "1";
	if(i==2)
		return "2";
		
	if(i==3)
		return "3";

	if(i==4)
		return "4";

	if(i==5)
		return "5";

	if(i==6)
		return "6";

	if(i==7)
		return "7";

	if(i==8)
		return "8";

	if(i==9)
		return "9";

}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int test;
	cin >> test;
	for(int cs=1;cs<=test;++cs)
	{
		string a;
		cin  >> a;
		vi cnt(26,0);
		repi(a.size())
		{
			cnt[a[i]-'A']++;
		}
		vi an(10,0);
		while(cnt['Z'-'A']>0)
		{
			an[0]++;
			cnt['Z'-'A']--;
			cnt['E'-'A']--;
			cnt['R'-'A']--;
			cnt['O'-'A']--;
		}
		while(cnt['W'-'A']>0)
		{
			an[2]++;
			cnt['T'-'A']--;
			cnt['W'-'A']--;
			cnt['O'-'A']--;
		}
		while(cnt['U'-'A']>0)
		{
			an[4]++;
			cnt['F'-'A']--;
			cnt['O'-'A']--;
			cnt['U'-'A']--;
			cnt['R'-'A']--;
		}
		while(cnt['F'-'A']>0)
		{
			an[5]++;
			cnt['F'-'A']--;
			cnt['I'-'A']--;
			cnt['V'-'A']--;
			cnt['E'-'A']--;
		}
		while(cnt['X'-'A']>0)
		{
			an[6]++;
			cnt['S'-'A']--;
			cnt['I'-'A']--;
			cnt['X'-'A']--;
		}
		while(cnt['V'-'A']>0)
		{
			an[7]++;
			cnt['S'-'A']--;
			cnt['E'-'A']-=2;
			cnt['V'-'A']--;
			cnt['N'-'A']--;
		}
		while(cnt['G'-'A']>0)
		{
			an[8]++;
			cnt['E'-'A']--;
			cnt['I'-'A']--;
			cnt['G'-'A']--;
			cnt['H'-'A']--;
			cnt['T'-'A']--;
		}
		while(cnt['O'-'A']>0)
		{
			an[1]++;
			cnt['O'-'A']--;
			cnt['N'-'A']--;
			cnt['E'-'A']--;
		}
		while(cnt['R'-'A']>0)
		{
			an[3]++;
			cnt['T'-'A']--;
			cnt['H'-'A']--;
			cnt['R'-'A']--;
			cnt['E'-'A']-=2;
		}
		an[9]=cnt['I'-'A'];

		string ans="";
		for(int i=0;i<10;++i)
		{
			for(int j=0;j<an[i];++j)
				ans += str(i);
		}
		
		cout << "Case #" << cs <<": " << ans << endl;
	}

  	return 0;
}

