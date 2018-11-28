#include <iostream>
#include <cstdio>
#include <string.h>
#include <cstring>
using namespace std;
#define sd(x) scanf("%d",&x)

char arr[101];
int check[26];
int check1[26];
char a[101];
char b[101];

int main() {
	int t;
	sd(t);
	int test = 0;
	while(t--) {
		int count = 0;
		test++;
		printf("Case #%d: ",test);
		int a,b,k;
		sd(a);sd(b);sd(k);
		for(int i = 0; i < a; i++) {
			for(int j = 0; j < b; j++) {
				if((i & j) < k) count++;
			}
		}
		printf("%d\n",count);
	}
	return 0;
}