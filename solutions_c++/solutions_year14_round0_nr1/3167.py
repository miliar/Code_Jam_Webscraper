#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <utility>
#include <vector>

using namespace std;

int main() {
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		int fQ; cin >> fQ;
		vector<vector<int> > fV(4,vector<int>());
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				int v; cin >> v;
				fV[i].push_back(v);
			}
		}
		int sQ; cin >> sQ;
		vector<vector<int> > sV(4,vector<int>());
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				int v; cin >> v;
				sV[i].push_back(v);
			}
		}
		vector<int> v1 = fV[fQ-1];
		vector<int> v2 = sV[sQ-1];
		map<int,int> m;
		for (int i = 0; i < v1.size(); i++) m[v1[i]]++;
		for (int i = 0; i < v2.size(); i++) m[v2[i]]++;
		int ans = -1;
		for (map<int,int>::iterator it = m.begin(); it != m.end(); it++) {
			if (it->second == 2) {
				if (ans != -1) {
					ans = -2;
					break;
				}
				ans = it->first;
			} 
		}
		cout << "Case #" << t << ": ";
		if (ans == -2) cout << "Bad magician!" << endl;
		else if (ans == -1) cout << "Volunteer cheated!" << endl;
		else cout << ans << endl;
	}
	return 0;
}