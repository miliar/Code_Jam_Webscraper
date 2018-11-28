#include<cstdio>
#include<cstring>
#include<iostream>
#include<cmath>
using namespace std;
#define N 105
int T;
char s[N];

inline char get_c(char ch){
	return ch == '+'?'-':'+';
}

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &T);
	int Case = 0;
	int i, j, k;
	int ans = 0;
	while (T --){
		
		ans = 0;
		scanf("%s", s);
		int len = strlen(s);
		for (i = len - 1; i >= 0; i --){
			if (s[i] == '-'){
				for (int j = 0; j <= i; j ++){
					s[j] = get_c(s[j]);
				}
				ans ++;
			}
		}
		printf("Case #%d: %d\n", ++ Case, ans);
		
	}
	return 0;
}
