#include <iostream>
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

int main()
{
    int cas, idx = 0;

    cin >> cas;
    while (cas--) {
        int n;
		char ch;
		int ans = 0;
		int total = 0;

        cin >> n;
		for (int i = 0; i < n + 1; i++) {
			cin >> ch;
			int d = ch - '0';

			if (total < i) {
				ans = max(ans, i - total);
			}

			total += d;
		}

        cout << "Case #" << ++idx << ": " << ans << endl;
    }

    return 0;
}
