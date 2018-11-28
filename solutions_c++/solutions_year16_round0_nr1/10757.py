#include <bits/stdc++.h>
#define endl '\n'

#define int long long

using namespace std;
const int MAXN = (int)(1e7);

int n;

void read()
{
	cin >> n;	
}

void solve()
{
	int mask = 0, s = 0, d;
	for(int i = 1; i <= MAXN; i++)	
	{
		s += n;
		d = s;
		while(d)
		{
			mask |= (1ll << (int)(d % 10));
			d /= 10;
		}
			
		if(mask == ((1ll << 10ll) - 1ll))
		{
			cout << s << endl;
			return;
		}
	}

	cout << "INSOMNIA" << endl;
}

#undef int
int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int T;
	cin >> T;

	for(int test = 1; test <= T; test++)
	{
		read();
		cout << "Case #" << test << ": ";
		solve();
	}

	return 0;
}

