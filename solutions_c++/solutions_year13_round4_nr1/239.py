#include <cmath>
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

#define MOD 1000002013

int t, n, m;
fstream in, out;
vector<pair<int, int> > start;
vector<pair<int, int> > exitloc;

int costhelp(int stations) {
	long long num = stations;
	long long ret = num * ((long long)(2 * n - num + 1)) / 2;
	ret = ret % MOD;
	return ret;
}
int cost(int stations, int people) {
	long long unit_cost = costhelp(stations);
	long long ret = unit_cost * ((long long) people);
	ret = ret % MOD;
	return ret;
}

bool comp(pair<int, int> a, pair<int, int> b) {
	return (a.first < b.first);
}

int main() {
	in.open("A-large.in", fstream::in);
	out.open("proba-large.out", fstream::out);

	in >> t;
    for (int i = 0; i < t; i++) {
		in >> n >> m;
		start.clear();
		exitloc.clear();
		int o, e, p;
		for (int j = 0; j < m; j++) {
			in >> o >> e >> p;
			start.push_back(make_pair(o, p));
			exitloc.push_back(make_pair(e, p));
		}
			
		int init_cost = 0;
		for (int j = 0; j < m; j++) {
			init_cost = (init_cost + cost(exitloc[j].first - start[j].first, start[j].second)) % MOD;
		}
		sort(start.begin(), start.end(), comp);
		sort(exitloc.begin(), exitloc.end(), comp);	
		
	
		int min_cost = 0;
		vector<int> num_left;
		for (int j = 0; j < m; j++) {
			num_left.push_back(start[j].second);
		}
		for (int j = 0; j < m; j++) {
			int departed = 0;
			int last;
			for (int k = 0; k < m; k++) {
				if (start[k].first <= exitloc[j].first) {
					last = k;
				}
			}
			for (int k = last; k >= 0; k--) {
				if (num_left[k] + departed <= exitloc[j].second) {
					departed += num_left[k];
					min_cost = (min_cost + cost(exitloc[j].first - start[k].first, num_left[k])) % MOD;
					num_left[k] = 0;
				} else {
					min_cost = (min_cost + cost(exitloc[j].first - start[k].first, exitloc[j].second - departed)) % MOD;
					num_left[k] -= exitloc[j].second - departed;
					break;
				}
			}
		}
		int ans = (init_cost - min_cost + MOD) % MOD;

		out << "Case #" << i + 1 << ": " << ans << endl;
	}
    
	in.close();
	out.close();

	return 0;
}
