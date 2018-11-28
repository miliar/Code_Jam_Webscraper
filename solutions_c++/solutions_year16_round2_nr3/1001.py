#include <bits/stdc++.h>

#define ft first
#define st second
#define mp make_pair
#define pb push_back
#define sz(n) int(n.size())


using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

const int N = 1e3 + 123;
const int inf = 1e9 + 7;
const ll INF = 1e18 + 7;

int t;
pair <string, string> s[N];


void solve(int x)
{
	int n, ans = 0;            
	cin >> n;

	int q = 100000;

	for (int i = 0; i < n; i ++)
	{
		cin >> s[i].ft >> s[i].st;
	}
	while (q --)
	{
		map <string, int> fir, sec;
		random_shuffle(s, s + n);
		int cur = 0;
		for (int i = 0; i < n; i ++)
		{
			//cout << fir[s[i].ft] << " " << sec[s[i].st] << endl;
			if (fir[s[i].ft] >= 1 && sec[s[i].st] >= 1) cur ++;
			else
			{
				fir[s[i].ft] ++;
				sec[s[i].st] ++;
			}
		}
		ans = max(ans, cur);
	}
	cout << "Case #" << x << ": "<< ans << endl;
}

int main ()
{
	srand(5);
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> t;
	for (int i = 1; i <= t; i ++)
	{
	//	cerr << i << endl;
		solve(i);
	}
	return 0;
}