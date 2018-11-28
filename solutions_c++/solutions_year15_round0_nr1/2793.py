#include <stdio.h>
 
int main() 
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d",&T);
	for (int i=1; i<=T; i++) {
		int n, count=0, ret=0;
		char M[1010]={0};
		scanf("%d %s",&n, M);
		for (int j=0; M[j]; j++) {
			int m = M[j]-'0';
			if (count < j) {
				ret += j-count;
				count += j-count;
			}
			count += m;
		}
		printf("Case #%d: %d\n",i, ret);
	}



}