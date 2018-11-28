
#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <utility>
#include <set>
#include <vector>

using namespace std;

int adjmat[111][111];
int color[111];
int visited[111];
int _N;

bool dfs(int node, int c) {
	if (color[node] != 0 && color[node] != c) {
		return false;
	}
	color[node] = c;
	visited[node] = 1;
	for (int i = 0; i < _N; i++) {
		if ((adjmat[node][i] || adjmat[i][node]) && !visited[i]) {
			dfs(i, c);
		}
	}
	return true;
}

int main()
{
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		int N; cin >> N;
		_N = N;
		vector<string> data;
		map<char,int> inner;
		map<char,int> firstInner;
		bool okAll = true;
		for (int i = 0; i < N; i++) {
			string str; cin >> str;
			char last = '{';
			string res;
			for (int j = 0; j < str.size(); j++) {
				if (str[j] != last) {
					res += str[j];
				}
				last = str[j];
			}
			if (res.size() > 1 && res[0] == res[res.size()-1]) {
				okAll = false;
			}
			if (res.size() > 1) {
				firstInner[res[0]]++;
				if (firstInner[res[0]] > 1) {
					okAll = false;
				}
			}
			data.push_back(res);
		}
		if (!okAll) {
			cout << "Case #" << t << ": 0\n";
			continue;
		}
		memset(color,0,sizeof(color));
		memset(adjmat,0,sizeof(adjmat));
		/*
		for (int i = 0; i < data.size(); i++) {
			cout << data[i] << endl;
		}
		*/
		// build the graph
		for (int i = 0; i < data.size(); i++) {
			for (int j = 0; j < data.size(); j++) {
				if (data[i][data[i].size()-1] == data[j][0]) {
					//cout << "joining " << data[i] << " -> " << data[j] << endl;
					adjmat[i][j] = 1;	 // must join
				}
			}
		}
		int curColor = 1;
		memset(color,0,sizeof(color));
		
		for (int i = 0; i < data.size(); i++) {
			for (int j = 1; j < data[i].size()-1; j++) {
				inner[data[i][j]]++;
				if (inner[data[i][j]] > 1) {
					okAll = false;
					break;
				}
			}
			if (!okAll) break;
		}
		if (okAll) {
			for (map<char,int>::iterator it = inner.begin(); it != inner.end(); it++) {
				for (int j = 0; j < data.size(); j++) {
					if (data[j][0] == it->first || data[j][data[j].size()-1] == it->first) {
						okAll = false;
						break;
					}
				}
				if (!okAll) break;
			}
		}
		// transform all
		map<string,int> check;
		for (int i = 0; i < data.size(); i++) {
			string str; str += data[i][0]; str += data[i][data[i].size()-1];
			data[i] = str;
			//cout << data[i] << endl;
			check[data[i]]++;
		}
		for (map<string,int>::iterator it = check.begin(); it != check.end(); it++) {
			string str = it->first; reverse(str.begin(), str.end());
			if (it->second > 1 && str != it->first) {
				okAll = false;
				break;
			}
			if (str != it->first && check.count(str) != 0) {
				okAll = false;
				break;
			}
		}
		if (!okAll) {
			cout << "Case #" << t << ": 0\n";
			continue;
		}
		for (int i = 0; i < data.size(); i++) {
			if (color[i] > 0) {
				continue;
			}
			memset(visited,0,sizeof(visited));
			bool ok = dfs(i, curColor);
			if (!ok) {
				okAll = false;
				break;
			}
			curColor++;
		}
		if (!okAll) {
			cout << "Case #" << t << ": 0\n";
			continue;
		}
		long long ans = okAll ? 1 : 0;
		for (int i = 1; i < curColor; i++) {
			map<string,int> mappings;
			//cout << "COLOR " << i << endl;
			for (int j = 0; j < N; j++) {
				if (color[j] == i) {
					mappings[data[j]]++;
				}
			}
			for (map<string,int>::iterator it = mappings.begin(); it != mappings.end(); it++) {
				long long cnt = 1;
				//cout << "string " << it->first << " cycle " << it->second << endl;
				for (int j = 1; j <= it->second; j++) {
					cnt = (cnt * j) % 1000000007LL;
				}
				ans = (ans * cnt) % 1000000007LL;
			}
		}
		//cout << "Num Color: " << curColor << endl;
		for (int i = 1; i < curColor; i++) {
			ans = (ans * i) % 1000000007LL;
		}
		cout << "Case #" << t << ": " << ans << "\n";
	}

	return 0;
}
