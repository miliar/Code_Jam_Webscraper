#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <set>

using namespace std;
int casenum,T;
int m, n;
int worst;
int num;
string trie[10];
int arr[10];
int cnt[5];

void dfs(int dep) {
	if (dep == m+1){
		for (int i = 1; i <= n; i++)
			if (cnt[i] == 0)
				return;
		int cnt = 0;
		for (int i = 1; i <= n; i++){
			set<string> s;
			s.clear();
			for (int j = 1; j <= m; j++) {
				if (arr[j] != i) continue;
				for (int k = 0; k <= trie[j].length(); k++)
					s.insert(trie[j].substr(0, k));
			}
			cnt += s.size();
		}
		if (cnt == worst) {
			num++;
		}
		else if (cnt > worst) {
			worst = cnt;
			num = 1;
		}
		return;
	}
	for (int i = 1; i <= n; i++) {
		arr[dep] = i;
		cnt[i]++;
		dfs(dep+1);
		cnt[i]--;
	}
}

int main() {
	freopen("gcj14.in","r",stdin);
//	/freopen("gcj14.out","w",stdout);
	cin >> T;
	for (casenum = 1; casenum <= T; casenum++) {
		cout << "Case #" << casenum << ": ";
		cin >> m >> n;
		for (int i = 1; i <= m; i++)
			cin >> trie[i];
		memset(cnt, 0, sizeof(cnt));
		worst = 0;
		dfs(1);
		cout<<worst << " " <<num;

		cout << endl;
	}
	return 0;
}
