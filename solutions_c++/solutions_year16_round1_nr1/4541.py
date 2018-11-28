
#include <algorithm>
#include <map>
#include <vector>
#include <iostream>
#include <cstring>
#include <string>
using namespace std;

#define loop(_i, _n) for( _i = 0; _i < _n; _i++)
#define loopi(_i, _n, _s) for( _i = _s; _i < _n; _i++)

vector<string> res;

void solve(char c, string d, string s, int i, int l)
{
	if (i++ < l)
	{
		solve(s[i], c + d, s, i, l);
		solve(s[i], d + c, s, i, l);
	}
	else
	{
		res.push_back(d);
	}
}

int main(int argc, char* argv[]) {
	freopen("C:\\Users\\Beauty\\Downloads\\A-small-attempt0.in", "r", stdin);
	freopen("out0.txt", "w", stdout);

	int num_case, t;
	cin >> num_case; num_case++;

	int N, J, nj;
	string s;

	loopi(t, num_case, 1) {
		cin >> s;

		solve(s[1], s.substr(0, 1), s, 1, s.length());
		sort(res.begin(), res.end());

		cout << "Case #" << t << ": " << res[int(res.size()) - 1] << endl;
		res.erase(res.begin(), res.begin() + res.size());
	}

	return 1;
}