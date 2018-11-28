#include<stdio.h>
#include<string.h>
using namespace std;
char s[2010];
int w[20];
int a[1000];
int flag;
int l;
void dfs(int pos) {
	if (pos == l) {
		flag = 1;
		for (int i = 0; i < 10; i++) {
			while (w[i]) {
				printf("%d", i);
				w[i]--;
			}
		}
		return;
	}
	if (pos >= l)
		return;
	if (flag)
		return;
	if (pos + 3 < l && a['Z'] && a['E'] && a['R'] && a['O']) {
		w[0]++;
		a['Z']--;
		a['E']--;
		a['R']--;
		a['O']--;
		dfs(pos + 4);
		if (flag)
			return;
		w[0]--;
		a['Z']++;
		a['E']++;
		a['R']++;
		a['O']++;
	}
	if (pos + 2 < l && a['S'] && a['I'] && a['X']) {
		w[6]++;
		a['S']--;
		a['I']--;
		a['X']--;
		dfs(pos + 3);
		if (flag)
			return;
		w[6]--;
		a['S']++;
		a['I']++;
		a['X']++;
	}
	if (pos + 2 < l && a['O'] && a['N'] && a['E']) {
		w[1]++;
		a['O']--;
		a['N']--;
		a['E']--;
		dfs(pos + 3);
		if (flag)
			return;
		w[1]--;
		a['O']++;
		a['N']++;
		a['E']++;
	}
	if (pos + 2 < l && a['T'] && a['W'] && a['O']) {
		w[2]++;
		a['T']--;
		a['W']--;
		a['O']--;
		dfs(pos + 3);
		if (flag)
			return;
		w[2]--;
		a['T']++;
		a['W']++;
		a['O']++;
	}
	if (pos + 4 < l && a['T'] && a['H'] && a['R'] && a['E'] > 1) {
		w[3]++;
		a['T']--;
		a['H']--;
		a['R']--;
		a['E'] -= 2;
		dfs(pos + 5);
		if (flag)
			return;
		w[3]--;
		a['T']++;
		a['H']++;
		a['R']++;
		a['E'] += 2;
	}
	if (pos + 3 < l && a['F'] && a['O'] && a['U'] && a['R']) {
		w[4]++;
		a['F']--;
		a['O']--;
		a['U']--;
		a['R']--;
		dfs(pos + 4);
		if (flag)
			return;
		w[4]--;
		a['F']++;
		a['O']++;
		a['U']++;
		a['R']++;
	}
	if (pos + 3 < l && a['F'] && a['I'] && a['V'] && a['E']) {
		w[5]++;
		a['F']--;
		a['I']--;
		a['V']--;
		a['E']--;
		dfs(pos + 4);
		if (flag)
			return;
		w[5]--;
		a['F']++;
		a['I']++;
		a['V']++;
		a['E']++;
	}
	if (pos + 4 < l && a['S'] && a['E'] > 1 && a['V'] && a['N']) {
		w[7]++;
		a['S']--;
		a['E'] -= 2;
		a['V']--;
		a['N']--;
		dfs(pos + 5);
		if (flag)
			return;
		w[7]--;
		a['S']++;
		a['E'] += 2;
		a['V']++;
		a['N']++;
	}
	if (pos + 4 < l && a['E'] && a['I'] && a['G'] && a['H'] && a['T']) {
		w[8]++;
		a['E']--;
		a['I']--;
		a['G']--;
		a['H']--;
		a['T']--;
		dfs(pos + 5);
		if (flag)
			return;
		w[8]--;
		a['E']++;
		a['I']++;
		a['G']++;
		a['H']++;
		a['T']++;
	}
	if (pos + 3 < l && a['N'] > 1 && a['I'] && a['E']) {
		w[9]++;
		a['N'] -= 2;
		a['I']--;
		a['E']--;
		dfs(pos + 4);
		if (flag)
			return;
		w[9]--;
		a['N'] += 2;
		a['I']++;
		a['E']++;
	}
}
int main() {
	int T;
	int cas = 1;
	scanf("%d", &T);
	while (T--) {
		flag = 0;
		memset(a, 0, sizeof(a));
		memset(w, 0, sizeof(w));
		printf("Case #%d: ", cas++);
		scanf("%s", s);
		l = strlen(s);
		for (int i = 0; i < l; i++) {
			a[s[i]]++;
		}
		dfs(0);
		printf("\n");
	}
	return 0;
}
