#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>

using namespace std;
typedef long long ll;

int num[105];

int main(){
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int n,t,a;
	scanf("%d", &t);
	for(int _ = 1; _ <= t; ++_){
		printf("Case #%d: ", _);
		scanf("%d %d", &a, &n);
		for(int i = 0; i < n; ++i) scanf("%d", num+i);
		sort(num, num+n);
		int at = 0;
		while(at < n){
			if(num[at] < a) a += num[at++];
			else break;
		}
		if(at == n) printf("0\n");
		else{
			int resp = n-at;
			int ad = 0;
			if(a > 1)
			while(at < n){
				while(a <= num[at]){
					a += a-1;
					ad++;
				}
				a += num[at];
				at++;
				resp = min(resp, ad+ n-at);
				//printf("atual: (%d) ad:%d falta:%d\n", a, ad, n-at);
				
			}
			printf("%d\n", resp);
			
		}
		
	}
	return 0;
}
