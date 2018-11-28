#include <bits/stdc++.h>
using namespace std;

int main(){
	freopen("large.in","r",stdin);
	freopen("large.out","w",stdout);
	int t,cs = 1;
	cin >> t;
	while(t--){
		string s;
		int k;
		cin >> s >> k;
		int n = s.length();
		int cn = 0;
		for (int i=0;i<=n-k;i++){
			if (s[i]=='-'){
				for (int j=i;j<i+k;j++){
					s[j] = s[j]=='-'?'+':'-';
				}
				cn++;
			}
		}
		int flag = 0;
		for (int i=n-k;i<n;i++){
			if (s[i]=='-') flag = 1;
		}
		printf("Case #%d: ",cs++);
		if (flag) printf("IMPOSSIBLE\n");
		else printf("%d\n",cn);
	}
	return 0;
}