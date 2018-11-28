#include <iostream>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <cstring>
#include <cstring>
#include <cctype>
#include <cstdlib>

using namespace std;

typedef vector<int> vi; 
typedef vector<vi > vvi; 
typedef pair<int,int> ii; 
typedef vector<ii > vii;
typedef vector<vii > vvii;
typedef set<ii > sii;

#define pb(x) push_back(x)
#define all(c) (c).begin(),(c).end()
#define ins(c) inserter((c),(c).begin())
#define mp(x,y) make_pair((x),(y))
#define mt(x,y,z) make_tuple((x),(y),(z))
#define INF (1e9)

ostream& operator<<(ostream& out, vi v)
{
    for (auto a: v)
        out << a << " ";
    return out;
}

ostream& operator<<(ostream& out, ii d)
{
    out << d.first << ", " << d.second << " ";

    return out;
}

string neg(string str)
{
	if (str[0] == '-')
		return str.substr(1);
	
	return "-" + str;
}

#define maxn 9

map<vi, int> M;

int solve(vi &v)
{
	int ans = 0;
	int max_val = 0;
	int count = 0; 
	
	auto p = M.find(v);
	if (p != M.end())
		return p->second;

	for (int i = 0; i < v.size(); i++)
		if (v[i]) {
			max_val = i;
			count += v[i];
		}
	
	ans = max_val;
	
	if (count && max_val > 3) {
		int a = max_val;
		for (int b = 1; b < a; b++) {
			int c = a - b;
				v[a]--;
				v[b]++;
				v[c]++;
				ans = min(ans, solve(v) + 1);
				v[a]++;
				v[b]--;
				v[c]--;
		}
	}
	
	// cout << "v " << v << ", ans " << ans << endl;
	M[v] = ans;
	return ans;
}

int main()
{
    int T, cas = 0;

    cin >> T;
    while (T--) {
		int n;

		cin >> n;
		vi v(maxn + 1);
		while (n--) {
			int a;
			cin >> a;
			v[a]++;
		}

		// cout << "v " << v << endl;
		int ans = solve(v);
		cout << "Case #" << ++cas << ": " << ans << endl;
    }

    return 0;
}
