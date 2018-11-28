#include <bits/stdc++.h>
using namespace std;

char S[101];

int givelen(int len) {
	int yet = 0;
	int ans = 0;
	for(int i=0; i<len; i++) {
		if(S[i] == '+')
			yet = 1;
		else {
			if(yet == 0)	
				ans++;
			else
				ans += 2;
			while(i<len && S[i] == '-')
				i++;
			i--;
			yet = 0;
		}
	}
	return ans;
}

int main() {
	int t;
	scanf("%d", &t);
	for(int tc=1; tc<=t; tc++) {
		scanf("%s", S);
		int len = strlen(S);

		int ans = givelen(len);
		printf("Case #%d: %d\n", tc, ans);
	}
}