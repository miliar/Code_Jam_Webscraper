#pragma comment(linker, "/STACK:108777216")
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <deque>
#include <algorithm>
using namespace std;

int const MAX_N = 32;
int const MAX_CH = 100100;

int n, FND = 0;
int cnt[MAX_N], sum = 0;
char st[MAX_CH];
vector<string> ans, loc_sol;

string make_str(int a, int b) {
	string ans = "";
	if (a >= 0)
		ans += (char) 'A' + a;
	if (b >= 0)
		ans += (char) 'A' + b;
	return ans;
}

void rec(int mv) {
	if (FND) return;

	if (sum <= 0) {
		ans = loc_sol;
		FND = 1;
		return;
	}

	for (int i=0; i<n; i++)
		if (cnt[i]*2 > sum)
			return;

	int mx_1 = -1, mx_2 = -1;
	for (int i=0; i<n; i++)
		if (cnt[i] > 0) {
			if (cnt[i] >= mx_1) {
				mx_2 = mx_1;
				mx_1 = cnt[i];
			}
			else if (cnt[i] >= mx_2) {
				mx_2 = cnt[i];
			}
		}

	for (int i=0; i<n; i++)
		if (cnt[i] && (cnt[i] == mx_1 || cnt[i] == mx_2))
			for (int j=i; j<n; j++)
				if (cnt[j] && (cnt[j] == mx_1 || cnt[j] == mx_2)) {
					cnt[i]--;
					cnt[j]--;

					if (cnt[i] >= 0 && cnt[j] >= 0) {
						sum -= 2;
						loc_sol.push_back(make_str(i,j));

						rec(mv+1);
						if (FND)
							return;

						sum += 2;
						loc_sol.pop_back();
					}

					cnt[i]++;
					cnt[j]++;
				}	

	for (int i=0; i<n; i++)
		if (cnt[i] && (cnt[i] == mx_1 || cnt[i] == mx_2)) {
			cnt[i]--;

			sum--;
			loc_sol.push_back(make_str(i,-1));

			rec(mv+1);
			if (FND)
				return;

			sum++;
			loc_sol.pop_back();

			cnt[i]++;
		}
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	gets(st);
	int tst_count;
	sscanf(st,"%d",&tst_count);
	for (int qqq=1; qqq<=tst_count; qqq++) {
		printf("Case #%d:",qqq);

		//
		scanf("%d",&n);
		sum = 0;
		FND = 0;
		for (int i=0; i<n; i++) {
			scanf("%d",&cnt[i]);
			sum += cnt[i];
		}
		ans.clear(); loc_sol.clear();
		rec(0);
		for (int i=0; i<(int) ans.size(); i++) printf(" %s",ans[i].c_str());
		//

		printf("\n");
	}
	return 0;
}