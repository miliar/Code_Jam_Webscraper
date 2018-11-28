#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <queue>
#include <utility>
#include <string>
#include <map>
#include <sstream>
using namespace std;

#define range(i,a,b) for(int i = (a), _n = (b); i < _n; ++i)
#define fo(i,n) range(i,0,n)
#define pb push_back

typedef pair<int,int> pr;

const int MAX_N = 210, MAX_K = 51000;
const int S = 0, T = 1;
int N, K;
bool seen[MAX_K];
vector<pr> edges;
vector<int> adj[MAX_K];

bool DFS(int node) {
	if (node == T) return true;
	if (seen[node]) return false;
	seen[node] = true;
	fo(i, adj[node].size()) if(DFS(adj[node][i])) {
		edges.pb(pr(node, i));
		return true;
	}
	return false;
}

bool augment() {
	fo(i,K) seen[i] = false;
	edges.clear();
	if (!DFS(S)) return false;
	fo(i,edges.size()) {
		int node = edges[i].first, ind = edges[i].second;
		int next = adj[node][ind];

		swap(adj[node][ind], adj[node][adj[node].size()-1]);
		adj[node].pop_back();
		adj[next].pb(node);
	}
	return true;
}

int solve() {
	int F = 0;
	while(augment()) ++F;
	return F;
}

int main() {
	int T;
	cin >> T;
	range(testCase, 1, T+1) {
		cin >> N;
		K = N;
		map<string, int> words;
		fo(i, MAX_K) adj[i].clear();
		fo(i,N) {
			string line("");
			while (line.size() == 0 || line[0] < 'a' || line[0] > 'z') getline(cin, line);
			stringstream stream(line);
			string word;
			while (stream >> word) {
				if (!words.count(word)) {
					words[word] = K;
					adj[K].pb(K+1);
					K += 2;
				}
				int w = words[word];
				adj[i].pb(w);
				adj[w+1].pb(i);
			}
		}
		cout << "Case #" << testCase << ": " << solve() << endl;
	}
}