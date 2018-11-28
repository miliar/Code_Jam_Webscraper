#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;
const int maxn = 1000000;
typedef long long LL;

char s[105];
int main(){
	//freopen("1.in", "r", stdin);
	//freopen("2.out", "w", stdout);
	int t,ca=0;
	cin >> t;
	while (t--){
		scanf("%s",s);
		int n = strlen(s),ret=0;
		s[n] = '+';
		for (int i = 0; i < n; i++) if (s[i] != s[i + 1]) ret++;
		printf("Case #%d: %d\n", ++ca, ret);
	}
	return 0;
}