#include "stdio.h"
#include <iostream>
#include <fstream>

using namespace std;

const int maxn = 1024;

int num[maxn];

void init() {
	int i;
	int k;
	num[0] = 0;
	for(i = 1; i*i < maxn; i++) {
		int j = i*i;
		int len = 0;
		int dig[10];
		j = i;
		while(j) {
			dig[len++] = j % 10;
			j /= 10;
		}
		len--;
		for(j = 0; j < len; j++,len--) if(dig[j]!=dig[len]) break;
		if(j < len) {
			for(k = (i-1)*(i-1)+1; k <= i*i; k++) num[k] = num[k-1];
			continue;
		}
		len = 0; j = i*i;
		while(j) {
			dig[len++] = j % 10;
			j /= 10;
		}
		len--;
		for(j = 0; j < len; j++,len--) if(dig[j]!=dig[len]) break;
		for(k = (i-1)*(i-1)+1; k < i*i; k++) num[k] = num[k-1];
		if(j >= len) {
			//printf("%d\n", i);
			num[i*i] = num[(i-1)*(i-1)]+1;
		} else {
			num[i*i] = num[i*i-1];
		}
	}
	int j = (i-1) *(i-1) + 1;
	for(; j < maxn; j++) num[j] = num[j-1];
}

int main()
{
	ofstream out("nihao.txt");		
	int t, i, j;
	int a, b;
	init();
	scanf("%d", &t);
	for(i = 1; i <= t; i++) {
		scanf("%d%d", &a, &b);
		out << "Case #" << i << ": " << num[b]-num[a-1] << "\n";
	}
}