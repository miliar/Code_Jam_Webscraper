// David Wahler <dwahler@gmail.com>
// Google Code Jam submission: "Ticket Swapping"

#include <algorithm>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

#define D(x)

using namespace std;

typedef long long i64;

const i64 MOD = 1000002013;

int main() {
    int T;
    cin >> T;
    
    for (int testCase = 1; testCase <= T; testCase++) {
    	int N, M;
    	cin >> N >> M;

    	i64 original = 0;

    	map<int, i64> entries, exits;

    	for (int i = 0; i < M; i++) {
    		int o, e;
    		i64 p;

    		cin >> o >> e >> p;

    		i64 d = e-o;
    		i64 cost = (N*d - (d*d - d)/2);
    		i64 totalCost = ((p%MOD) * (cost%MOD)) % MOD;
    		D(cerr << "original:  " << p << " from " << o << " to " << e << " @ " << cost << " = " << totalCost << endl);

    		original += totalCost;
    		original = original % MOD;

    		entries[o] += p;
    		exits[e] += p;
    	}

    	i64 optimized = 0;

    	while (!entries.empty()) {
    		int to = exits.begin()->first;

    		map<int, i64>::iterator it = entries.upper_bound(to);
    		it--;
    		int from = it->first;

    		i64 p = min(entries[from], exits[to]);

    		i64 d = to - from;
    		i64 cost = (N*d - (d*d - d)/2);
    		i64 totalCost = ((p%MOD) * (cost%MOD)) % MOD;
    		D(cerr << "optimized: " << p << " from " << from << " to " << to << " @ " << cost << " = " << totalCost << endl);

    		optimized += totalCost;
    		optimized = optimized % MOD;

    		entries[from] -= p;
    		if (entries[from] == 0) entries.erase(from);
    		exits[to] -= p;
    		if (exits[to] == 0) exits.erase(to);
    	}

    	i64 result = (((original - optimized) % MOD) + MOD) % MOD;


        cout << "Case #" << testCase << ": ";
        cout << result;
        cout << endl;
    }
}
