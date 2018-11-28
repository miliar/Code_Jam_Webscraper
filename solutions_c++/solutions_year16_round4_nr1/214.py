#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <queue>

using namespace std;
const int inf = 1000000007;
int n , a , b , c;
string gao (int h, int who) {
	if(h == 0) {
		if(who == 0) {
			return "R";
		}
		else if (who == 1) {
			return "P";
		}
		else return "S";
	}
	string A = gao(h - 1, who);
	string B = gao (h - 1, (who + 2) % 3);
	if (A < B) return A + B;
	else return B + A;
}
int main () {
	// freopen ("input.txt", "r" , stdin);
	// freopen ("output.txt", "w", stdout);
	int t, cas = 0;scanf ("%d" , &t);	
	while (t --) {
		scanf ("%d %d %d %d", &n , &a, &b , &c);
		vector<string> ans;
		for(int i = 0 ; i < 3 ; i ++) {
			string ret = gao(n , i);
			int A = 0 , B = 0 , C = 0;
			for(int j = 0 ; j < (int)ret.size() ; j ++) {
				if (ret[j] == 'R') A ++;
				else if (ret[j] == 'P') B ++;
				else C ++;
			}
			if (a == A && b == B && c == C) {
				ans.push_back(ret);
			}
		}
		printf ("Case #%d: ", ++ cas);
		if (ans.size() == 0) puts ("IMPOSSIBLE");
		else {
			sort(ans.begin(), ans.end());
			printf("%s\n", ans[0].c_str());
		}
	}

	return 0;
}