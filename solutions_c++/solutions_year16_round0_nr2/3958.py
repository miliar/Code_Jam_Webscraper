#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef pair<int, int> PII;

int main(){
	int times;
	scanf("%d\n", &times);
	for (int t=1; t<=times; t++){
		char s[200];
		gets(s);
		int len = strlen(s);
		char pre = '+', now = '+';
		int cnt = 0;
		for (int i=len-1; i>=0; i--){
			now = s[i];
			if (now != pre){
				cnt++;
				pre = now;
			}
		}
		printf("Case #%d: %d\n", t, cnt);
	}
	return 0;
}
