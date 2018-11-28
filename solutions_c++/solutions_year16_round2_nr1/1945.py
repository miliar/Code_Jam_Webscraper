#include <bits/stdc++.h>
using namespace std;
typedef long long int LL;
char s[21010], ans[21010];
int ansLen = 0, cnt[500];
void f(char c, int len) {
	for(int i=0 ; i<len ; i++) ans[ansLen++] = c;
}
int main() {
	int T;
	scanf("%d", &T);

	for(int caso=1 ; caso<=T ; caso++) {
		scanf("%s", s);
		int len = strlen(s);
		memset(cnt, 0, sizeof(cnt));
		for(int i=0 ; i<len ; i++) {
			cnt[s[i]]++;
		}
		ansLen = 0;
		//ZERO
		cnt['E'] -= cnt['Z'];
		cnt['R'] -= cnt['Z'];
		cnt['O'] -= cnt['Z'];
		f('0', cnt['Z']);
		cnt['Z'] = 0;
		//TWO
		cnt['T'] -= cnt['W'];
		cnt['O'] -= cnt['W'];
		f('2', cnt['W']);
		cnt['W'] = 0;
		//FOUR
		cnt['F'] -= cnt['U'];
		cnt['O'] -= cnt['U'];
		cnt['R'] -= cnt['U'];
		f('4', cnt['U']);
		cnt['U'] = 0;
		//SIX
		cnt['S'] -= cnt['X'];
		cnt['I'] -= cnt['X'];
		f('6', cnt['X']);
		cnt['X'] = 0;
		//EIGHT
		cnt['E'] -= cnt['G'];
		cnt['I'] -= cnt['G'];
		cnt['H'] -= cnt['G'];
		cnt['T'] -= cnt['G'];
		f('8', cnt['G']);
		cnt['G'] = 0;
		//ONE
		cnt['N'] -= cnt['O'];
		cnt['E'] -= cnt['O'];
		f('1', cnt['O']);
		cnt['O'] = 0;
		//THREE
		cnt['H'] -= cnt['T'];
		cnt['R'] -= cnt['T'];
		cnt['E'] -= cnt['T'];
		cnt['E'] -= cnt['T'];
		f('3', cnt['T']);
		cnt['T'] = 0;
		//FIVE
		cnt['I'] -= cnt['F'];
		cnt['V'] -= cnt['F'];
		cnt['E'] -= cnt['F'];
		f('5', cnt['F']);
		cnt['F'] = 0;
		//SEVEN
		cnt['E'] -= cnt['S'];
		cnt['V'] -= cnt['S'];
		cnt['E'] -= cnt['S'];
		cnt['N'] -= cnt['S'];
		f('7', cnt['S']);
		cnt['S'] = 0;
		//SEVEN
		f('9', cnt['I']);
		ans[ansLen] = '\0';
		sort(ans, ans + ansLen);
		printf("Case #%d: %s\n", caso, ans);
	}
	return 0;
} 
