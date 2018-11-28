#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cstring>
#include <cassert>
#include <utility>
#include <iomanip>
#include <bitset>

using namespace std;

const int INF = (int) 1e6;

int tn;
int n;
bitset <1250> mask[25];   
string s;
map <string, int> mp;
int num;
int ans;
bitset <1250> a, b;

void go(int pos, bitset <1250> a, bitset <1250> b) {
	if (pos == n + 1) {
		a = a & b;
		ans = min(ans, (int) a.count());
		return;
	}
	if (pos == 1)
		go(pos + 1, a | mask[pos], b);
	else if (pos == 2) 
		go(pos + 1, a, b | mask[pos]);
	else {
		go(pos + 1, a | mask[pos], b);
		go(pos + 1, a, b | mask[pos]);
	}
}

int main() {
	//assert(freopen("input.txt","r",stdin));
	//assert(freopen("output.txt","w",stdout));

	scanf("%d", &tn);

	for (int test = 1; test <= tn; test++) {
		scanf("%d\n", &n);

		mp.clear();
		for (int i = 1; i <= n; i++)
			mask[i] = 0;
		num = 0;

		for (int i = 1; i <= n; i++) {
			getline(cin, s);
			string word = "";
			for (int j = 0; j < (int) s.length(); j++) {
				if (s[j] >= 'a' && s[j] <= 'z') {
					word.append(1, s[j]);
				}
				else {
					if (word != "") {
						int cur;
						if (mp.count(word) == 0) {
							num++;
							mp[word] = num;
							cur = num;
						}
						else
							cur = mp[word];
						mask[i].set(cur);		
					}
					word = "";
				}
			}
			if (word != "") {
				int cur;
				if (mp.count(word) == 0) {
					num++;
					mp[word] = num;
					cur = num;
				}
				else
					cur = mp[word];
				mask[i].set(cur);		
			}
		}

		ans = INF;

		a = 0; b = 0;
		go(1, a, b);

		printf("Case #%d: %d\n", test, ans);
	}

	return 0;
}                       