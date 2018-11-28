#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;
char a[1003];
int main() {
	int t;
	char str[1003];
	scanf("%d",&t);
	for(int i=1; i<=t;i++) {
		scanf("%s",str);
		int l = strlen(str);
		char first = str[0];
		int x=0,m1=0,m2=0;
		a[0]=str[0];
		for(int j=1;j<l;j++) {
			if(str[j]>=a[0]) {
				for(int k=j;k>0;k--) {
					a[k]=a[k-1];
				}
				a[0]=str[j];
			} else {
				a[j]=str[j];
			}
		}
		printf("Case #%d: ",i);
		for(int j=0;j<l;j++) {
			printf("%c",a[j]);
		}
		printf("\n");
	}
	return 0;
}