#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main (){
	int cc;
	cin >> cc;
	for(int i=0; i<cc; i++) {
		printf("Case #%d: ",i+1);
		int n,nset,c,ans;
		scanf("%d",&n);
		nset=c=0;
		if(n==0) {
			printf("INSOMNIA\n");
			continue;
		}
		while(nset != 1023) {
			c++;
			int x = n*c;
			ans = x;
			while(x) {
				nset |= 1<<(x%10);
				x/=10;
			}
		}
		printf("%d\n",ans);
	}
}
