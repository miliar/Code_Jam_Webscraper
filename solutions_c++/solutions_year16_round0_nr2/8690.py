#include <bits/stdc++.h>

using namespace std;

const int MAX_N = 11;

int best[1 << MAX_N];

int n;

bool getBit(int conf, int j) {
	return conf & (1 << j);
}

void setBit(int &conf, int j) {
	conf |= (1 << j);	
}

void unsetBit(int &conf, int j) {
	conf &= ~(1 << j);
}

void flipBit(int &conf, int j) {
	conf ^= (1 << j);
}

void swapBit(int &conf, int i, int j) {
	bool a = getBit(conf, i),
   b = getBit(conf, j);

	if(a) {
	setBit(conf, j);
}	else {
	unsetBit(conf, j);
}
	if(b) {
	setBit(conf, i);
} 	else {
	unsetBit(conf, i);
}
}

int flip(int conf, int j) {
    int st = 0;
    int dr = j;

    while(st < dr) {
	flipBit(conf, st);
	flipBit(conf, dr);

	swapBit(conf, st, dr);

        ++st;
        --dr;
    }


	if(st == dr) {
		flipBit(conf, st);
	}

    return conf;
}

void BFS(int now) {
    best[now] = 0;
    queue<int> Q;
    Q.push(now);
    while(!Q.empty()) {

        now = Q.front();
        Q.pop();

        for(int i = 0; i < n; ++i) {

            int nxt = flip(now, i);

            if(best[now] + 1 < best[nxt]) {
                best[nxt] = best[now] + 1;
                Q.push(nxt);
            }
        }
    }
}

int main() {
    int T;
    cin >> T;
    for(int i = 1; i <= T; ++i) {
        cout << "Case #" << i << ": ";

        string s;
        cin >> s;

	s += "+";

	int sol = 0;

	for(int j = 0; j < s.length() - 1; ++j) {
		sol += s[j] != s[j + 1];
	}
	cout << sol << "\n";

    }
    return 0;
}
