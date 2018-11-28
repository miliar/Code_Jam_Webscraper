#include <bits/stdc++.h>
using namespace std;

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("test.out","w", stdout);
	int test, n;
	char s[1111];

	scanf("%d", &test);
	for (int i=1; i<= test; i++){
		scanf("%d ", &n);
		for (int j=0; j < n+1; j++){
			scanf("%c", &s[j]);
		}
		int j = 0, carry =0, res=0;
		while (j < n+1) {
			if (carry < j) {
				res+= (j-carry);
				carry+= (j-carry);
			}
			carry+= (s[j]-48);
			j++;
		}
		printf("Case #%d: %d\n", i, res);
	}
}