#include <bits/stdc++.h>
#define SZ(v) ((int)(v).size())

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;

char s[1003];

int main(){
	int t;
	scanf("%d", &t);
	for (int tt=1; tt<=t; tt++){
		int k;
		scanf("%s%d", s, &k);
		int n = (int) strlen(s);
		int cnt = 0;
		for (int i=0; i<=n-k; i++){
			if (s[i] == '-'){
				for (int j=0; j<k; j++){
					s[i+j] = '-' + '+' - s[i+j];
				}
				cnt++;
			}
		}
		bool suc = true;
		for (int i=n-k+1; i<n; i++){
			if (s[i] == '-'){
				suc = false;
				break;
			}
		}
		if (suc){
			printf("Case #%d: %d\n", tt, cnt);
		}
		else {
			printf("Case #%d: IMPOSSIBLE\n", tt);
		}
	}
	return 0;
}