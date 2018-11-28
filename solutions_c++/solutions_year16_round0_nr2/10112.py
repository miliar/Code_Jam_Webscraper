#include <iostream>
#include <string>
#include <algorithm>
#include <list>
#include <stdio.h>
#include <vector>
#include <stack>
#include <queue>
#include <bitset>
#include <set>
#include <cmath>
#include <map>
#include <string.h>
#include <cassert>

using namespace std;


#define ALL(v)  v.begin(), v.end()
#define SZ(v)   ((int)(v.size()))
#define ALLR(v) v.rbegin(), v.rend()
#define pii pair<int,int>
#define pb push_back
#define Int long long
#define ull unsigned long long
#define mp make_pair
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)

inline void end(string s){cout << s; exit(0);}
inline void end(Int n){cout << n; exit(0);}

Int mod(Int a, Int b) {
	return (((a % b) + b) % b);
}
const double PI = acos(-1);

const int N = 1e5 + 5;


inline bool is_goal(string &s) {
	return s.size() == count(s.begin(), s.end(), '+');
}

struct state {
	string stk;
	int level;
	state(string s, int l) {
		stk = s;
		level = l;
	}
};


string flip(int to, string s) {
	for(int i=0; i <= to; i++) {
		if (s[i] == '+') s[i] = '-';
		else s[i] = '+';
	}
	reverse(s.begin(), s.begin() + to + 1);
	return s;
}

int main(){
#ifndef ONLINE_JUDGE
	freopen("code.in","r", stdin);
	freopen("code.out", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	
	
	for (int i = 0; i < t; ++i)
	{
		int test_case = i + 1;
		map<string, int> vis;

		string s;
		cin >> s;

		queue<state> q;
		q.push(state(s, 0));\
		vis[s] = 1;

		while(q.size()) {
			state u = q.front();
			q.pop();
			string stk = u.stk;
			int level = u.level;
			int last_index = stk.size() - 1;

			if(is_goal(stk)) {
				printf("Case #%d: %d\n", test_case, level);
				goto next;
			}
			while(stk[last_index] == '+') last_index--;

			for(int i=0; i <= last_index; i++) {
				string flipped = flip(i, stk);
				if (vis[flipped]) continue;
				if (is_goal(flipped)) {
					printf("Case #%d: %d\n", test_case, level + 1);
					goto next;
				}
				q.push(state(flipped, level+1));
				vis[flipped] = 1;
			}
		}

		next:;
	}
	return 0;
}
