#include <iostream>
#include <cstdio>
#include <algorithm>
#include <queue>
using namespace std;

int main() {
	int t;
	scanf("%d", &t);
	int freq[2501];
	for(int i=1; i<=t; i++){
		for(int j=0; j<=2500; j++) freq[j]=0;
		int n, m, k=1;
		scanf("%d", &n);
		for(int j=0; j<n*(2*n-1); j++){
			scanf("%d", &m);
			freq[m]++;
		}
		printf("Case #%d: ", i);
		for(int j=0; j<=2500 && k<=n; j++){
			if(freq[j]%2==1){
				printf("%d%c", j, (k==n)?'\n':' ');
				k++;
			}
		}
	}
	return 0;
}
