#include <bits/stdc++.h>
using namespace std;
//look at my code my code is amazing
#define FOR(i, a, b) for (int i = int(a); i < int(b); i++)
#define FOREACH(it, a) for (typeof(a.begin()) it = (a).begin(); it != (a).end(); it++)
#define ROF(i, a, b) for (int i = int(a); i >= int(b); i--)
#define REP(i, a) for (int i = 0; i < int(a); i++)
#define INF 1000000000
#define INFLL 1000000000000000000LL
#define ALL(x) x.begin(), x.end()
#define MP(a, b) make_pair((a), (b))
#define X first
#define Y second
#define EPS 1e-9
#define DEBUG(x)   cerr << #x << ": " << x << " "
#define DEBUGLN(x) cerr << #x << ": " << x << " \n"
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef long long ll;
typedef vector<bool> vb;
//ios_base::sync_with_stdio(0);//fast entrada/salida ;-)
//cin.tie(NULL); cout.tie(NULL);

void solve()
{
	static int caso = 0;
	string s_in;
	deque<char> s_out;

	cin >> s_in;

	s_out.push_back(s_in[0]);

	FOR(i, 1, s_in.size())
	{
		if(s_in[i] >= s_out[0])
			s_out.push_front(s_in[i]);
		else
			s_out.push_back(s_in[i]);
	}

	cout << "Case #" << ++caso << ": ";

	REP(i, s_out.size())
		cout << s_out[i];

	cout << '\n';
}

int main()
{
	ios_base::sync_with_stdio(0);//fast entrada/salida ;-)
	cin.tie(NULL); cout.tie(NULL);
	int T;

	cin >> T;

	REP(i, T)
		solve();

	return 0;
}