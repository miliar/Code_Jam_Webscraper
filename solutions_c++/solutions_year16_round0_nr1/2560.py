#include <cstdio>
#include <algorithm>
#include <functional>
#include <set>
#include <map>
#include <vector>
#include <iostream>

using namespace std;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int cases = 0;
	scanf("%d",&cases);
	for(int casenum = 1; casenum <= cases; casenum++) {
		int digits[10]={0};
		long long n;
		scanf("%lld",&n);
		if (n==0) {
			printf("Case #%d: INSOMNIA\n", casenum);
			continue;
		}
		int seen = 0;
		int i=1,r;
		while(seen < 10) {
			long long t = i*n;
			while(t) {
				r = t % 10;
				if(!digits[r]) {
					seen++;
				}
				digits[r]++;
				t/=10;
			}
			i++;
		}
		printf("Case #%d: %lld\n", casenum, n*(i-1));
	}
	return 0;
}