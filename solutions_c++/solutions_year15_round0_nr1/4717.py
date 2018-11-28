#include<bits/stdc++.h>
using namespace std;

int T, n;
char s[1005];
int main(){
    scanf("%d", &T);
    for(int qwe=1; qwe<=T;qwe++){
	scanf("%d%s", &n, s);
	int sum[1005], ans = 0;
	for(int i=0; i<1005;i++) sum[i] = 0;
	sum[0] = s[0]-'0';
	for(int i=1; i<=n; i++){
	    sum[i] = sum[i-1] + (s[i]-'0');
	    if(s[i] != '0' && sum[i-1] < i) ans = max(ans, i-sum[i-1]);
	}
	printf("Case #%d: %d\n", qwe, ans);
    }
    return 0;
}
