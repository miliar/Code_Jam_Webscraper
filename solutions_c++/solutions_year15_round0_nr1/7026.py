#include <bits/stdc++.h>
using namespace std;
#define FOR(i,k,n) for(int i = (k); i < (n); i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(a) begin(a),end(a)
#define MS(m,v) memset(m,v,sizeof(m))
#define D10  fixed<<setprecision(10)
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> P;
typedef long long ll;
const ll INF = 114514810;
const ll MOD = 1000000007;
const double EPS = 1e-8;
const double PI = acos(-1.0);
struct edge
{
	int from, to, cost;
	bool operator < (const edge& e) const { return cost < e.cost; }
	bool operator >(const edge& e) const { return cost > e.cost; }
};
int dx[] = { -1, 0, 0, 1 }; int dy[] = { 0, -1, 1, 0 };
///*************************************************************************************///
///*************************************************************************************///
///*************************************************************************************///

int main()
{
	int n;
	cin >> n;
	for (int Case = 0; Case < n;Case++)
	{
		int m; cin >> m;
		string s; cin >> s;
		int cnt = 0;
		int ans = 0;
		REP(i, m + 1)
		{
			int k = s[i] - '0';
			if (cnt < i)
			{
				ans += i - cnt;
				cnt = i;
			}
			cnt += k;
		}
		cout << "Case #" << Case + 1 << ": " << ans << endl;
	}
	return 0;
}