#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;

#define READLINE() while(getchar()!='\n');

typedef long long LL;

char s[110];

void resolve(int id){
	scanf("%s", s);
	int l = strlen(s);
	int ans = 0;
	for (int i = l-1; i >= 0; --i) {
		if ((s[i] == '-') && (ans % 2 == 0)) {
			++ans;	
		} else if ((s[i] == '+') && (ans % 2 == 1)) {
			++ans;
		}
	}
	printf("Case #%d: %d\n", id, ans);
}

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	READLINE();
	for (int i = 1; i <= T; ++i) {
		resolve(i);	
	}
	fclose(stdout);
	fclose(stdin);
	return 0;	
}
