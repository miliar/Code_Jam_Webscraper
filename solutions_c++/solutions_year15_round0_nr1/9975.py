#include <iostream>
#include <stdio.h>
using namespace std;
int main(){
	int cases;
	scanf(" %d", &cases);
	for(int c=0;c<cases;c++){
		int max;
		char a[1000];
		int n, k;
		scanf("%d %s\n", &max, a);
		n=k=0;
		for(int i=0;i<=max && a[i]!=0;i++){
			if((n+k)<i &&  a[i]!='0')
				k+=i-(n+k);
			n+=a[i]-'0';
		}
		printf("Case #%d: %d\n", c+1, k);
	}
}