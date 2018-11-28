#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) rep2(i,0,n)
#define rep2(i,m,n) for(int i=m;i<(n);++i)

int TC,n,cur,ans;
string s;
char in[1010];

int main(){
    scanf("%d",&TC);
    rep(tc,TC){
	cur=ans=0;
	printf("Case #%d: ", tc+1);
	scanf("%d %s", &n, in);
	s = in;
	for (int i = 0; i <= n; ++i) {
	    int a = s[i] - '0';
	    if (cur >= i) cur += a;
	    else {
		ans += i - cur;
		cur = i + a;
	    }
	}
	printf("%d\n", ans);
    }
    return 0;
}
