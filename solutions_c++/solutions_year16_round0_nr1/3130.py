#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;
const int maxn = 1000005;
typedef long long LL;

/*char s[105];
int main(){
	//freopen("1.in", "r", stdin);
	//freopen("2.out", "w", stdout);
	int t,cc=0;
	scanf("%d", &t);
	while (t--){
		scanf("%s",s);
		int len=strlen(s),ans=0;
		s[len] = '+';
		for (int i = 0; i < len; i++) if (s[i] != s[i + 1]) ans++;
		printf("Case #%d: %d\n", ++cc, ans);
	}
	return 0;
}*/
int bb[maxn],s;
int main(){
	//freopen("1.in", "r", stdin);
	//freopen("out.out", "w", stdout);
	int m = 1023;
	for (int i = 1; i < maxn; i++){
		s = 0;
		for (int j = i; s < m; j += i){
			int k = j;
			while (k){
				int u = k % 10;
				s |= (1 << u);
				k /= 10;
			}
			bb[i] = j;
		}
	}
	int t,cc=0;
	scanf("%d", &t);
	while (t--){
		scanf("%d", &m);
		printf("Case #%d: ", ++cc);
		if (m == 0) printf("INSOMNIA\n");
		else printf("%d\n", bb[m]);
	}
	return 0;
}

