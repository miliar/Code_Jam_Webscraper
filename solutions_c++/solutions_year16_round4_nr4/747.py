#include <bits/stdc++.h>

#define debug(x)
#define fori(i, ini, lim) for(int i = int(ini); i < int(lim); i++)
#define ford(i, ini, lim) for(int i = int(ini); i >= int(lim); i--)

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> ii;

int N;

string to_bin(int x) {
	string bin = "";
	while(x) {
		bin += (x & 1) + '0';
		x >>= 1;
	}
	reverse(bin.begin(), bin.end());
	return bin;
}

int main() {
	ios_base::sync_with_stdio(false);

	int kase = 1;
	int t;
	cin >> t;
	while(t--) {
		cin >> N;
		string s;
		int original = 0;
		vector<string> v;
		fori(i, 0, N) {
			cin >> s;
			v.push_back(s);
		}
		int cnt = 0;
		ford(i, v.size() - 1, 0) {
			ford(j, v[i].size() - 1, 0) {
				if(v[i][j] == '1') {
					original |= (1 << cnt);
				}
				cnt++;
			}
		}
		int best = 1 << 30;
		fori(i, 0, (1 << (N * N))) {
			debug(to_bin(i));
			if((original & i) != original) {
				continue;
			}
			vector<int> workers;
			int counter = N * N - 1;
			int working_workers = 0;
			fori(j, 0, N) {
				int cur = 0;
				fori(k, 0, N) {
					if(i & (1 << counter)) {
						cur |= (1 << (counter % N));
					}
					counter--;
				}
				workers.push_back(cur);
				working_workers += (cur != 0);
			}
			int working_machines = 0;
			vector< vector<int> > machines(N + 5);
			bool deu_bom = true;
			fori(j, 0, N) {
				fori(k, 0, N) {
					int cur = workers[k];
					if(cur & (1 << j)) {
						machines[j].push_back(cur);
					}
				}
				if(!machines[j].empty()) {
					if(__builtin_popcount(machines[j][0]) != (int) (machines[j].size())) {
						deu_bom = false;
					}
				}
				fori(k, 1, machines[j].size()) {
					if(machines[j][k] != machines[j][k - 1] || __builtin_popcount(machines[j][k]) != (int) (machines[j].size())) {
						deu_bom = false;
						break;
					}
				}
				working_machines += (machines[j].size() > 0);
			}
			if(deu_bom && working_machines == N && working_workers == N) {
				debug(i);
				debug(best);
				best = min(best, __builtin_popcount(original ^ i));
				debug(best);
			}
		}
		cout << "Case #" << kase++ << ": " << best << '\n';
	}

	return 0;
}
