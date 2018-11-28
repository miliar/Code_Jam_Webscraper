#include <bits/stdc++.h>
#include <unordered_map>

using namespace std;

#define mp make_pair
#define fi first
#define sc second

string flip(string st, int x) {
	string ret = "";
	for (int i=x; i>=0; i--) {
		if (st[i]=='+') ret+='-';
		else ret+='+';
	}
	for (int i=x+1; i<st.length(); i++) ret+=st[i];
	return ret;	
}

bool ready(string st) {
	for (int i=0; i<st.length(); i++)
		if (st[i]=='-') return false;
	return true;
}

int BFS(string st) {

	unordered_map<string, bool> flag;
	queue<pair<string,int> > q;
	q.push(mp(st, 0));
	while (!q.empty()) {
		pair<string, int> u = q.front();
		q.pop();
		string s = u.fi;
		if (ready(s)) return u.sc;
		if (u.sc >= 100000) return -1;		
		if (!flag[s]) {				
			flag[s] = true;
			for (int i=0; i<s.length(); i++) {
				string temp = flip(s, i);
				q.push(mp(temp, u.sc+1));
			}
		}
	}
	return -1;
}



int main() {
	freopen("B-small.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int tc=1; tc<=t; tc++) {
		printf("Case #%d: ", tc);
		string st;
		cin>>st;		
		printf("%d\n", BFS(st));
	}
	return 0;
}