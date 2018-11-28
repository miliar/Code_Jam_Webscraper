#include <iostream>
#include <vector>
#include <algorithm>
#include <hash_map>
#include <map>

using namespace std;
using namespace stdext;

typedef __int64 ll;
typedef unsigned __int64 ull;

int T, A, N;
vector<int> v;

map<pair<int, int>, int> cache2;


int solve(int have, int i) {
	if (i == N) return 0;
	pair<int, int> key = make_pair(have, i);
	map<pair<int, int>, int>::iterator it = cache2.find(key);
	if (it != cache2.end()) return it->second;
	if (v[i] < have) return cache2[key] = solve(have + v[i], i + 1);
	int res1 = 1 + solve(have, i + 1);
	if (have <= 1) return cache2[key] = res1;
	int res2 = 1 + solve(have + have - 1, i);
	return cache2[key] = min(res1, res2);
}

int main(int argc, char* argv[]) {
    cin >> T;
    for (int t_ = 0; t_ != T; ++t_) {
		cache2.clear();
		cin >> A >> N;
		v.resize(N);
		for (int n = 0; n != N; ++n)
			cin >> v[n];
		sort(v.begin(), v.end());
        cout << "Case #" << (t_ + 1) << ": " << solve(A, 0) << "\n";
    }
    return 0;
}
