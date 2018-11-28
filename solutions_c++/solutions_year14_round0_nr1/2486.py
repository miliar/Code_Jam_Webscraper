//venk13
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <fstream>
#include <cassert>

using namespace std;

#define sz(a) (int)(a.size())
#define len(a) (int)(a.length())
#define pb push_back
#define mp make_pair

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, cas = 1; cin >> t;
	while(t--) {
		cout << "Case #" << cas++ << ": ";
		int cnt[17] = {0};
		for(int i = 0; i < 2; i++) {
			int rr; cin >> rr; rr--;
			for(int j = 0; j < 4; j++)
				for(int k = 0; k < 4; k++) {
					int aa; cin >> aa;
					if(j == rr)
						cnt[aa]++;
				}
		}
		bool morethanOne = 0, none = 1, found = 0; int my = -1;
		for(int i = 1; i < 17; i++) {
			if(cnt[i] == 2) {
				if(found)
					morethanOne = 1;
				my = i;
				found = 1;
				none = 0;
			}
		}
		if(none)
			cout << "Volunteer cheated!";
		else if(morethanOne)
			cout << "Bad magician!";
		else
			cout << my;
		cout << '\n';
	}
	return 0;
}