#include <bits/stdc++.h>

using namespace std;

int main(){
	int t,n;
	int ans,cur;
	string s;
	scanf("%d",&t);
	for (int jj=1; jj<=t; jj++){
		cin >> n >> s;
		ans = 0;
		cur = (s[0]-'0');
		for (int i=1; i<=n; i++){
			if (cur < i){
				ans += (i-cur);
				cur = i;
			}
			cur += (s[i]-'0');
		}
		printf("Case #%d: %d\n",jj,ans);
	}
	return 0;
}
