#include <iostream>
#include <stdio.h>
using namespace std;
int dig[11];
int digits(int n) {
	while(n>0) {
		int d = n%10;
		dig[d]++;
		n=n/10;
	}
	for(int i=0; i<10;i++) {
		if(dig[i]==0) return 0;
	}
	return 1;	
}
int main() {
	int x,n,c=1;
	cin>>x;
	while(x--) {
		cin>>n;
        if(n==0) {
        	 printf("Case #%d: INSOMNIA\n",c++);
        	 continue;
        }
		int num=n;
		for(int i=0; i<10;i++) dig[i]=0;
		while(!digits(num)) {
			num = num + n;
		}
        printf("Case #%d: %d\n",c++,num);
	}
	return 0;
}
