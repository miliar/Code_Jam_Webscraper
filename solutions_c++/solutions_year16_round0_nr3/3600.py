#include <bits/stdc++.h>
using namespace std;
//@author Vidur Katyal
#define endl '\n'
#define pb push_back
#define mp make_pair
typedef long long LL;
typedef pair <int, int> pii;
typedef pair <int, pii> piii;
typedef vector <int> vi;
typedef vector < pii > vpii;
#define DEBUG(x) cerr<<#x<<": "<<x<<endl;
#define FAST1 ios_base::sync_with_stdio(0)
#define FAST2 cin.tie(0);cout.tie(0); cerr.tie(0)
const long double PI = acos(-1.0);
const long double EPS = 1e-9;
const LL MOD = 1000000007;
const LL MAXN = 100010;

LL convert(int i)
{
	string s = "";
	while(i)
	{
		if(i%2)
			s += '1';
		else
			s += '0';
		i /= 2;
	}
	LL x = 0;
	for(int i = s.length()-1; i >= 0; --i)
		x = x*10 + s[i]-'0';
	return x;
}

LL cnvt(LL x, int b)
{
	LL y = 0;
	LL i = 1;
	while(x)
	{
		y += (x%10)*i;
		i *= b;
		x /= 10;
	}
	return y;
}

LL divisor(LL n)
{
	LL rt = sqrt(n);
	for(LL i = 2; i <= rt; ++i)
		if(n%i == 0)
			return i;
	return -1;
}

int main()
{
	FAST1;
	FAST2;
	int T;
	cin>>T;
	for (int t = 1; t <= T; ++t)
	{
		int n, j;
		cin>>n>>j;
		vector <LL> res;
		vector < vector<LL> > res2;
		LL st = 1 + (1<<(n-1));
		LL end = 1<<n;
		for (LL i = st; i < end; i += 2)
		{
			LL x = convert(i);
			vector <LL> divs;
			for (int j = 2; j <= 10; ++j)
			{
				LL y = cnvt(x, j);
				LL d = divisor(y);
				if(d == -1)
					break;
				divs.pb(d);
			}
			if(divs.size() != 9)
				continue;
			res.pb(x);
			res2.pb(divs);
			if(res.size() == j)
				break;
		}
		cout<<"Case #"<<t<<":\n";
		for (int i = 0; i < res.size(); ++i)
		{
			cout<<res[i]<<" ";
			for (int j = 0; j < res2[i].size(); ++j)
				cout<<res2[i][j]<<" ";
			cout<<endl;
		}
	}
	return 0;
}