#include <iostream>
#include <cstdio>
using namespace std;

char dict[10];
char tar[10];
int len;
int k, l, s;
int max_;

char tmp[10];

int gou(int pos){
	if (pos == s) {
		int ans = 0;
		for(int i = 0; i + l <= s; i++) {
			bool flag = 1;
			for (int j = 0; j < l; j++) {
				if (tmp[i + j] != tar[j]) {
					flag = 0;
					break;
				}
			}
			if (flag) ans++;
		}
		max_ = max(max_, ans);
		return ans;
	}
	else {
		int ans = 0;
		for (int i = 0; i < k; i++){
			tmp[pos] = dict[i];
			ans += gou(pos + 1);
		}
		return ans;
	}
}

int main(){
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("b.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		scanf("%d %d %d", &k, &l, &s);
		scanf("%s %s", dict, tar);
		max_ = 0;
		int ans = gou(0);
		double res = ans;
		for (int i = 0; i < s; i++) res /= k;
		printf("Case #%d: %.6lf\n", t + 1, (double)max_ - res);
	}
    return 0;
}
