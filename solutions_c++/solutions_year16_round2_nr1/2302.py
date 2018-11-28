#include <cstdio>
#include <cstring>

char s[2005];

int order[10] = {0, 2, 6, 8, 3, 4, 1, 5, 7, 9};

char charac[10][10] = {
"ZERO",
"WTO",
"XIS",
"GHEIT",
"THREE",
"RFOU",
"ONE",
"FIVE",
"VSEEN",
"NINE"
};

void sol() {
	int cnt[30] = {0}, ans[30] = {0};
	scanf("%s", s);
	int l = strlen(s);
	for(int i = 0;i < l;i++)
		cnt[s[i] - 'A']++;
	for(int i = 0;i < 10;i++) {
		ans[order[i]] += cnt[charac[i][0] - 'A'];
		if(order[i] == 9) ans[order[i]] /= 2;
		for(int j = 1;j < strlen(charac[i]);j++) 
			cnt[charac[i][j] - 'A'] -= cnt[charac[i][0] - 'A'];
		cnt[charac[i][0] - 'A'] = 0;
	}
	for(int i = 0;i < 10;i++)
		for(int j = 0;j < ans[i];j++) printf("%d", i);
	putchar(10);
} 

int main() {
	int ks; scanf("%d", &ks);
	for(int i = 1;i <= ks;i++)
		printf("Case #%d: ", i), sol();
}
