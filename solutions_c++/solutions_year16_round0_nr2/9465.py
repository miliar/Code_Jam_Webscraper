#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int bfs(string start) {

	string target = string(start.size(),'+');

	int steps = 0;
	map<string, bool> vis;

	queue<string> q;
	q.push(start);
	vis[start] = true;
	while (!q.empty()) {

		int size = q.size();

		while (size--) {
			string top = q.front();
			q.pop();
			if(top == target){
				return steps;
			}
			string s = "";
			for (int i = 0; i < (int) top.size(); i++) {
				if (top[i] == '-') {
					s = '+' + s;
				} else {
					s = '-' + s;
				}
				string newString = s + top.substr(i+1);
				if (vis.find(newString) == vis.end()) {
					q.push(newString);
					vis[newString] = true;
				}
			}

		}
		steps++;

	}
	return steps;
}
int Case = 1, tc = 0;

int main() {
	freopen("B-small-attempt0.in", "rt", stdin);
	freopen("B-small-attempt0.out", "w", stdout);


	string s;
	cin >> tc;

	while (tc--) {
		cin >> s;
		cout << "Case #" << Case++ << ": " << bfs(s)  << endl;

	}

	return 0;
}
//By : mohamed waleed
