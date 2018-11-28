#include <bits/stdc++.h>

using namespace std;

inline int get(int mask, int pos)
{
    return (mask >> pos) & 1;
}

void solve(int T)
{
    int n;
    vector< vector<string> > W;
    map<string, int> number;
    scanf("%d\n", &n);
    W.resize(n);
    for (int i = 0; i < n; i++) {
	string line;
	getline(cin, line);

	stringstream q;
	q.str(line);

	string buf;
	while (q >> buf) {
	    W[i].push_back(buf);
	    number[buf] = 0;
	}
    }

    int CSDF = 0;
    map<string, int>::iterator it = number.begin();
    for (; it != number.end(); it++) {
	it->second = CSDF++;
    }

    vector< vector<int> > Q(n);
    for (int i = 0; i < n; i++) {
	Q[i].resize(W[i].size());
	for (int j = 0; j < W[i].size(); j++) {
	    Q[i][j] = number[W[i][j]];
	}
    }

    int maxmask = 1<<n;
    int bestans = INT_MAX;
    bool hasIn[2][CSDF];
    for (int mask = 0; mask < maxmask; mask++) {
	memset(hasIn, 0, sizeof(hasIn));
	if (get(mask, 0) != 0 || get(mask, 1) != 1) {
	    continue;
	}

	int cur = 0;
	for (int i = 0; i < n && cur < bestans; i++) {
	    int curset = get(mask, i);
	    for (int j = 0; j < Q[i].size() && cur < bestans; j++) {
		if (!hasIn[curset][Q[i][j]]) {
		    if (hasIn[1-curset][Q[i][j]]) {
			cur++;
		    }
		    hasIn[curset][Q[i][j]] = true;
		}
	    }
	}

	bestans = min(bestans, cur);
    }

    cout << "Case #" << T + 1 << ": " << bestans << "\n";
    cout.flush();
}

int main()
{
    int Q;
    scanf("%d", &Q);
    for (int T = 0; T < Q; T++) {
	solve(T);
    }
}
