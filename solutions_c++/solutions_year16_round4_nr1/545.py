#include <bits/stdc++.h>
using namespace std;

int T, Cas = 1, N, R, P, S;

vector<char> ch;
char pos[20];
bool vis[20];

char cmp(char a, char b) {
	if (a == 'P' && b == 'S') return 'S';
	if (a == 'S' && b == 'P') return 'S';
	if (a == 'P' && b == 'R') return 'P';
	if (a == 'R' && b == 'P') return 'P';
	if (a == 'S' && b == 'R') return 'R';
	if (a == 'R' && b == 'S') return 'R';
}

bool check() {
	vector<char> now, last;
	for (int i = 0; i < (1 << N); i ++) {
		now.push_back(pos[i]);
    }
	for (int i = N ; i >= 1; i --) {
		last = now;
		now.clear();
        for (int j = 0; j < (1 << i); j += 2) {
        	if (last[j] == last[j + 1]) {
        		return false;
            } else {
            	now.push_back(cmp(last[j], last[j + 1]));
            }
        }
    }
    return true;
}

vector<string> vs;

void dfs(int now) {
	if (now == (1 << N)) {
		pos[now] = '\0';
		if (check()) {
			vs.push_back(pos);
        }
		return ;
    }
    for (int i = 0; i < (1 << N); i ++) {
    	if (!vis[i]) {
    		pos[now] = ch[i];
    		vis[i] = true;
    		dfs(now + 1);
    		vis[i] = false;
        }
    }
}

void small_task() {
	vs.clear();
	ch.clear();
	memset(vis, 0, sizeof(vis));
    for (int i = 0; i < R; i ++) {
    	ch.push_back('R');
    }
    for (int i = 0; i < P; i ++) {
    	ch.push_back('P');
    }
    for (int i = 0; i < S; i ++) {
    	ch.push_back('S');
    }
    dfs(0);
    sort(vs.begin(), vs.end());
    if (vs.size() == 0) {
    	cout << "IMPOSSIBLE\n";
    } else {
    	cout << vs[0] << endl;
    }
}

string get(char c, int N) {
    if (N == 0) {
    	if (c == 'P') return "P";
    	if (c == 'S') return "S";
    	if (c == 'R') return "R";
    }
    if (c == 'S') {
    	string a = get('P', N - 1);
    	string b = get('S', N - 1);
    	if (a > b) {
    		return b + a;
    	} else {
    		return a + b;
        }
    }
    if (c == 'P') {
    	string a = get('P', N - 1);
    	string b = get('R', N - 1);
        if (a > b) {
        	return b + a;
        } else {
        	return a + b;
        }
    }
    if (c == 'R') {
    	string a = get('R', N - 1);
    	string b = get('S', N - 1);
    	if (a > b) {
    		return b + a;
        } else {
        	return a + b;
        }
    }
}

bool check(string s) {
	int pp = 0, ss = 0, rr = 0;
	for (int i = 0; i < s.length(); i ++) {
		if (s[i] == 'S') {
			ss ++;
        }
        if (s[i] == 'P') {
        	pp ++;
        }
        if (s[i] == 'R') {
        	rr ++;
        }
    }
    if (ss == S && pp == P && rr == R) {
    	return true;
    }
    return false;
}

void big_task() {
    string ps = get('P', N);
    string ss = get('S', N);
    string rs = get('R', N);
    vs.clear();
    if (check(ps)) {
    	vs.push_back(ps);
    }
    if (check(ss)) {
    	vs.push_back(ss);
    }
    if (check(rs)) {
    	vs.push_back(rs);
    }
    sort(vs.begin(), vs.end());
    if (vs.size() == 0) {
    	cout << "IMPOSSIBLE\n";
    } else {
    	cout << vs[0] << endl;
    }
}   
void work() {
	printf("Case #%d: ", Cas ++);
	scanf("%d %d %d %d", &N, &R, &P, &S);
	big_task();
}

int main() {
	scanf("%d", &T);
	while (T --) {
		work();
    }
	return 0;
}
