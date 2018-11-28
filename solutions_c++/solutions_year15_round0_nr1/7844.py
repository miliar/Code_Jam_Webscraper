#include <iostream>
#include <stdio.h>
#include <cmath>
#include <string>
#include <vector>
#include <limits>
#define MAX numeric_limits<int>::max()

using namespace std;

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int test = 0;
	int j;
	scanf("%d",&test);
	for(j = 1 ; j <= test ; j++){
		int n;
		scanf("%d",&n);
		int i;
		int ans = 0;
		int sum = 0;
		char str[n+2];
		scanf("%s",str);
		for(i = 0 ; i <= n ; i++) {
			if(sum > n)
				break;			
			int s = str[i] - 48;
			if(s > 0) {
				if(sum < i) {
					ans += i - sum;
					sum += (i-sum);
				}	
				sum += s;			
			}			
		}
		printf("Case #%d: %d\n",j,ans);
	}
	return 0;
}