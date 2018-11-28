#include <bits/stdc++.h>
using namespace std;
int st, tcs, n, len, ans;
char buf[10050];
int main(){
	scanf("%i", &tcs);
	for(int tc=1;tc<=tcs;tc++){
		scanf("%i", &n);
		ans = 0;
		st = 0;
		scanf("%s%n", buf, &len);
		for(int i=0;i<len-1;i++){
			if(st < i){ ans += (i - st); st = i;}
			st += (buf[i] - '0');
		}
		printf("Case #%i: %i\n", tc, ans);
	}
}