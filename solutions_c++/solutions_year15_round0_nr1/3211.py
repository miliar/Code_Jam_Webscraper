#include<cstdio>
#include<iostream>
#include<algorithm>
#include<queue>
using namespace std;
int TC, smax, ss[100000], n;
char str[1005];
int main(){
	scanf("%d", &TC);
	for(int tc = 1; tc <= TC; ++tc){
		scanf("%d", &smax);
		scanf("%s", str);
		n = 0;
		for(int i = 0; i <= smax; ++i){
			for(char j = '0'; j < str[i]; ++j) ss[n++] = i;
		}
		sort(ss, ss+n);
		int ct = 0, ans = 0;
		for(int i = 0; i < n; ++i){
			if(ct < ss[i]) ans += ss[i] - ct, ct = ss[i];
			++ct;
		}
		printf("Case #%d: %d\n", tc, ans);
	}
}