#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <string>
#include <sstream>
typedef long long ll;
using namespace std;

#define FORi(n) for(int i=0;i<n;++i)
#define FOR(i,a,b) for(int i=a;i<=b;++i)
#define mp make_pair
#define pb push_back
#define sz(x) int((x).size())

string inttostr (int a) {
    string s;
    ostringstream os;
    os << a;
    s = os.str();
    return s;
}

void solve () {
	int T = 0;
	cin >> T;
	for (int test_id = 1; test_id <= T; test_id++) {
		string res = "";
		int N, M;
		cin >> N >> M;
		vector< vector<int> > a (N, vector<int>(M, 0));
		vector< vector<int> > b (N, vector<int>(M, 0));
		for (int i = 0; i < N; ++i)
			for (int j = 0; j < M; ++j)
				cin >> a[i][j];

		vector<int> maxR (N, 0);
		vector<int> maxC (M, 0);
		for (int i = 0; i < N; ++i)
			for (int j = 0; j < M; ++j) {
				maxR[i] = max(maxR[i], a[i][j]);
				maxC[j] = max(maxC[j], a[i][j]);
			}

		for (int i = 0; i < N; ++i)
			for (int j = 0; j < M; ++j)
				b[i][j] = min( maxR[i], maxC[j]);

		res = "YES";
		for (int i = 0; i < N; ++i)
			for (int j = 0; j < M; ++j)
				if (a[i][j] != b[i][j]) res = "NO";

		cout << "Case #" << test_id << ": " << res << endl;
	}
}

void main()
{
    #ifdef _DEBUG
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
    #endif

    solve();
}