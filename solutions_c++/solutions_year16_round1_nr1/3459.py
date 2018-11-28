#include<cstdio>
#include<iostream>
#include<cstring>

using namespace std;

#define READLINE() while(getchar()!='\n')

char s[1010];
char ans[2020];

void solve(int id){
	gets(s);	
	int offset = 1010, l = 0, r = 1;
	ans[offset] = s[0];
	int len = strlen(s);
	for (int i = 1; i < len; ++i) {
		if (s[i] < ans[offset + l]) {
			ans[offset + r++] = s[i];	
		} else {
			ans[offset + (--l)] = s[i];	
		}
	}
	printf("Case #%d: ", id);
	for (int i = l; i < r; ++i) {
		putchar(ans[offset + i]);	
	}
	puts("");
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	READLINE();
	for (int i = 1; i <= T; ++i) {
		solve(i);	
	}
	fclose(stdin);
	fclose(stdout);
	return 0;	
}
