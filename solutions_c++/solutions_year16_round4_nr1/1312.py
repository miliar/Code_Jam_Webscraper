#include <iostream>
#include <iomanip>
#include <vector>
#include <set>
#include <cmath>
#include <string>
#include <algorithm>
#include <utility>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<char> vc;
typedef vector<vc> vvc;
typedef vector<string> vs;
typedef vector<vs> vvs;
typedef vector<double> vd;
typedef vector<bool> vb;
typedef vector<ll> vll;


string construct(int r, int p, int s) {

	//cout << "calling " << r << p << s << endl;
	
	if (r + p == 2 && s == 0)
		return "PR";
	if (r + s == 2 && p == 0)
		return "RS";
	if (p + s == 2 && r == 0)
		return "PS";

	char special;
	bool inc;
	if (r != s && r != p) {
		special = 'r';
		inc = (r > s);
	}
	if (s != r && s != p) {
		special = 's';
		inc = (s > p);
	}
	if (p != s && p != r) {
		special = 'p';
		inc = (p > r);
	}

	int pb = (r + p - s) / 2;
	int rb = (s + r - p) / 2;
	int sb = (p + s - r) / 2;

	//cout << "computed " << rb << " " << pb << " " << sb << endl;

	if (special == 'r' && inc)
		return construct(rb, rb, sb) + construct(rb, sb, rb);
	if (special == 'p' && inc)
		return construct(pb, pb, rb) + construct(rb, pb, pb);
	if (special == 's' && inc)
		return construct(pb, sb, sb) + construct(sb, pb, sb);
	if (special == 'r' && !inc)
		return construct(rb, sb, rb) + construct(rb, rb, sb);
	if (special == 'p' && !inc)
		return construct(rb, pb, pb) + construct(pb, pb, rb);
	if (special == 's' && !inc)
		return construct(sb, pb, sb) + construct(pb, sb, sb);
}

int main()
{	
	int t;
	cin >> t;
	int cas = 1;

	while (t--) {
		cout << "Case #" << cas << ": ";
		cas++;

		int n, r, p, s;
		cin >> n >> r >> p >> s;

		if ((abs(r - s) > 1) || (abs(r - p) > 1) || (abs(p - s) > 1))
			cout << "IMPOSSIBLE" << endl;
		else
			cout << construct(r, p, s) << endl;
		
	}
    return 0;
}
