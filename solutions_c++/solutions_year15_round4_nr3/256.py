#include <iostream>
#include <string>
#include <sstream>
#include <iterator>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
#include <map>

using namespace std;

vector<vector<pair<int,int>>> adj;
vector<bool> word;
vector<int> flow;
map<string,int> dict;
//map<int,string> di;

int toi(const string &s) {
	if (dict.count(s)) return dict[s];
	else {
		dict.insert(make_pair(s,adj.size()));
		//di.insert(make_pair(adj.size(),s));
		word.push_back(true);
		adj.push_back(vector<pair<int,int>>());
		return adj.size()-1;
	}
}

vector<bool> seen;
int target;
vector<int> path;
vector<int> pa;

bool dfs(int v) {
	if (v==target) return true;
	seen[v] = true;
	for (int i = 0;i<adj[v].size();i++) {
		auto e = adj[v][i];

		if (seen[e.first]) continue;

		int f = flow[e.second];
		if (word[v]) {
			if (f==-1) continue;
		}
		else {
			if (f==1) continue;
		}
		path.push_back(e.second);
		pa.push_back(e.first);
		if (dfs(e.first)) return true;
		path.pop_back();
		pa.pop_back();
	}
	return false;
}

bool improve() {
	target = 0;
	seen = vector<bool>(adj.size(),false);
	path.clear();
	pa.clear();

	bool res = dfs(1);
	if (!res) return false;

	//printf("path ");
	for (int i=0;i<path.size();i++) {
		//printf("(%d,%d:%d)",pa[i],path[i],flow[path[i]]);
	  //if (word[pa[i]]) printf("%s",di[pa[i]].c_str());
	  //printf(" ");
		if (i%2) {
			flow[path[i]]--;
		}
		else {
			flow[path[i]]++;
		}
	}
	//printf("\n");

	return true;
}

int main() {
  int T;

  cin >> T;

  for (int t=1;t<=T;t++) {
    int N;
    cin >> N;
		string line;
		getline(cin, line);

		adj = vector<vector<pair<int,int>>>(N);
		word = vector<bool>(N,false);
		flow = vector<int>();
		dict.clear();
//di.clear();

		for (int i=0;i<N;i++) {
			getline(cin, line);
			//cout << line << endl;
			vector<string> vec;
			istringstream iss(line);
			copy(istream_iterator<string>(iss),istream_iterator<string>(),back_inserter(vec));
			//for (auto s : vec) cout << s << ".";
			//cout << endl;
			for (auto s : vec) {
				// make new edge
				int wi = toi(s);
				int edge = flow.size();
				flow.push_back(0);
				adj[i].push_back(make_pair(wi,edge));
				adj[wi].push_back(make_pair(i,edge));
			}
		}

		int flo = 0;
		while(improve()) {
			//cout << "flo" << endl;
			flo++;
			//if (flo == 5) break;
		}

    printf("Case #%d: %d\n",t,flo);
  }

}


