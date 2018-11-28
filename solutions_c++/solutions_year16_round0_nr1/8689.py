#include <bits/stdc++.h>

#define TASK ""
#define sqr(x) ((x)*(x))
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
using namespace std;
const ll INFLL = numeric_limits<long long>::max();
const ll INFINT = numeric_limits<int>::max();
const ld EPS = 1e-7;
const ll MOD = 1e9 + 7LL;
const ll MAXN = 250000;

int run()
{
	ll val;
	ll k = 0;
	ll n;
	cin >> n;
	for(int j=0;j<n;j++)
	{
		cin >> val;
		ll cval = val;
		k++;
		ll ans = 0;
		bool used[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
		bool f = false;
		for (int i = 0; i < 1000; i++)
		{
			ll val2 = val;
			if (val2 == 0)used[0] = true;
			while (val2 != 0)
			{
				used[val2 % 10] = true;
				val2 /= 10;
			}
			bool flag = false;
			for (int i = 0; i < 10; i++)
			{
				if (!used[i])flag = true;
			}
			if (!flag)
			{
				cout << "Case #" << k << ": " << val << endl;
				f = true;
				break;
			}
			val += cval;
		}
		if(!f)
		{
			cout << "Case #" << k << ": INSOMNIA"<< endl;
		}
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);

#ifdef LOCAL
#ifdef STRESS
	freopen("input.txt","w",stdout);



#endif
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	if(strcmp(TASK,"")!=0)
	{
		freopen(TASK".in", "r", stdin);
		freopen(TASK".out", "w", stdout);
	}
#endif

	run();

	return 0;
}