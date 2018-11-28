#include <iostream>
#include <set>
#include <complex>
#include <cassert>
#include <vector>
#include <iomanip>
#include <sstream>
#include <map>

using namespace std;

typedef long long int Z;

string ts;
int N;
vector<map<int, Z>> cap;
int sz;
int source;
int sink;

Z huge = 1000000;

vector<bool> visited;

bool flow_(int v) {
	if(visited[v]) return false;
	visited[v] = true;
	if(v == sink) return true;
	for(auto p : cap[v]) {
		if(p.second && flow_(p.first)) {
			--cap[v][p.first];
			++cap[p.first][v];
			return true;
		}
	}
	return false;
}

bool flow() {
	visited.resize(sz);
	fill(visited.begin(), visited.end(), false);
	return flow_(source);
}

int main() {
	cin.sync_with_stdio(false);
	
	int Te;
	{
		getline(cin, ts);
		stringstream ss(ts);
		ss >> Te;
	}
	for(int T = 0; T < Te; ++T) {
		cap.clear();
		{
			getline(cin, ts);
			stringstream ss(ts);
			ss >> N;
		}
		int idx = 0;
		map<string, int> idxs;
		vector<vector<int>> sens;
		for(int i = 0; i < N; ++i) {
			getline(cin, ts);
			ts.push_back('\n');
			stringstream ss(ts);
			vector<int> sen;
			string w;
			while(true) {
				ss >> w;
				if(!ss.good()) break;
				if(idxs.count(w)) {
					sen.push_back(idxs[w]);
				} else {
					sen.push_back(idx);
					idxs[w] = idx++;
				}
			}
			sens.push_back(move(sen));
		}
		
		sz = 2 * idx + 2;
		cap.resize(sz);
		
		source = sz - 2;
		sink = sz - 1;
		
		vector<bool> a(idx);
		vector<bool> b(idx);
		for(int x : sens[0]) {
			a[x] = true;
		}
		for(int x : sens[1]) {
			b[x] = true;
		}
		
		Z res = 0;
		for(int i = 0; i < idx; ++i) {
			if(a[i] != b[i]) {
				if(a[i]) {
					cap[source][2 * i] = huge;
				} else {
					cap[2 * i + 1][sink] = huge;
				}
			} else if(a[i]) {
				++res;
			}
			if(!a[i] || !b[i]) {
				cap[2 * i][2 * i + 1] = 1;
			}
		}
		
		for(int s = 2; s < N; ++s) {
			for(int i : sens[s]) {
			for(int j : sens[s]) {
				if(i == j) continue;
				cap[2 * i + 1][2 * j] = huge;
			}
			}
		}
		
		while(flow()) ++res;
		
		cout << "Case #" << T + 1 << ": " << res << "\n";
	}
	
	return 0;
}
