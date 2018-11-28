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

set<ii> S3;
set<ii> S4;

bool solve(int X, int R, int C)
{
	if (X == 1)
		return true;
	
	if (X == 2) {
		if (R % 2 && C % 2)
			return false;
		else
			return true;
	}

	if (X == 3) {
		if (R < 3 && C < 3) {
			return false;
		} else {
			int a = max(R, C);
			int b = min(R, C);
			if (S3.count(mp(a,b)))
				return true;
			else
				return false;
		}
	}

	int a = max(R, C);
	int b = min(R, C);

	if (S4.count(mp(a,b)))
		return true;
	else
		return false;
}

void init()
{
	S3.insert(mp(3,2));
	S3.insert(mp(3,3));
	S3.insert(mp(4,3));

	S4.insert(mp(4,3));
	S4.insert(mp(4,4));
}

int main()
{
	int T, cas = 0;

	init();

	cin >> T;
	while (T--) {
		int X, R, C;
		cin >> X >> R >> C;
		string ans;
		if (solve(X, R, C))
			ans = "GABRIEL";
		else
			ans = "RICHARD";
		cout << "Case #" << ++cas << ": " << ans << endl;
	}

	return 0;
}
