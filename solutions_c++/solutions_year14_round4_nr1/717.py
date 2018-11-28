
#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

int main(){

	int testcase; scanf("%d", &testcase);
	int n, x;
	int s[1401];
	int keep;
	int ans;

	for(int t=1; t<=testcase; ++t){
		scanf("%d %d", &n, &x);
		for(int i=0; i<=1400; ++i){
			s[i] = 0;
		}
		for(int i=0; i<n; ++i){
			scanf("%d", &keep);
			s[keep] ++;
		}

		ans = 0;

		for(int i=x; i>0; --i){
			if(2*i <= x){
				ans += s[i]/2;
				s[i] = s[i]%2;
			}
			if(s[i]){
				ans += s[i];
				keep = s[i]; s[i] = 0;
				for(int j=x-i; j>0; --j){
					if(s[j] <= keep){
						keep -= s[j];
						s[j] = 0;
					}else{
						s[j] -= keep;
						break;
					}
				}
			}
		}

		printf("Case #%d: %d\n", t, ans);
	}
	return 0;	
}
