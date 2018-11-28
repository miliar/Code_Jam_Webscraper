#include <bits/stdc++.h>
using namespace std;

int main(){
	int t, n;
	scanf("%d",&t);
	for(int j=0; j<t; j++){
		scanf("%d",&n); n++;
		char a[n+1];
		gets(a);
		int count = 0;
		int total = 0;
		for (int i = 1; i <= n; ++i){
			if(total < i-1){
				count += i-1 - total;
				total = i-1;
			}
			total += a[i] - 48;
		}
		printf("Case #%d: %d\n",j+1, count);
	}
	return 0;
}