#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000;
const int MAXM = 1000;

int used[MAXN];
vector<int> edges[MAXN];
int match[MAXN];
int matchto[MAXM];

bool dfs_kuhn(int v) {
    used[v] = 1;

    for (int i = 0; i < edges[v].size(); i++) {
        int next = edges[v][i];

        if (matchto[next] == -1) {
            matchto[next] = v;
            match[v] = next;
            return true;
        }
        else if (!used[matchto[next]] && dfs_kuhn(matchto[next])) {
            matchto[next] = v;
            match[v] = next;
            return true;
        }
    }

    return false;
}

int match_kuhn(int n, int m) {
    fill(match, match + n, - 1);
    fill(matchto, matchto + m, - 1);

    int cnt = 0;

    for (int i = 0; i < n; i++) {
        fill(used, used + n, 0);

        if (dfs_kuhn(i)) {
            cnt++;
        }
    }

    return cnt;
}

void solve(){
	int n;
	cin >> n;

	map<string, int> mp1, mp2;
	int n1 = 0, n2 = 0;
	vector<pair<string, string> > edglist;
	for (int i = 0; i < n; i++) {
		string s1, s2;
		cin >> s1 >> s2;
		if (mp1.find(s1) == mp1.end()) {
			mp1[s1] = n1;
			n1++;
		}
		if (mp2.find(s2) == mp2.end()) {
			mp2[s2] = n2;
			n2++;
		}
		edglist.push_back(make_pair(s1, s2));
	}

	for (int i = 0; i < n1; i++) {
		edges[i].clear();
	}

	for (int i = 0; i < edglist.size(); i++) {
		edges[mp1[edglist[i].first]].push_back(mp2[edglist[i].second]);
	}

	cout << n - (n1 + n2 - match_kuhn(n1, n2));
}

int main(){
#ifdef HELTHAZAR
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int test;
	cin >> test;
	for (int t = 1; t <= test; t++) {
		//printf("Case #%d: ", t);
		cout << "Case #" << t << ": ";
		solve();
		cout << endl;
		//printf("\n");
	}
}
