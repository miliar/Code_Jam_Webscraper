#include "bits/stdc++.h"
using namespace std;
const int N = 1e3 + 5;
const int inf = 1e6 + 6;
int t;
char str[N];
int n , k;
int main(){
	scanf("%d" , &t);
	for(int i = 1 ; i <= t ; ++i){
		scanf("%s" , str + 1);
		scanf("%d" , &k);
		n = strlen(str + 1);
		printf("Case #%d: " , i);
		int ans = 0;
		for(int i = n ; i >= k ; --i){
			if(str[i] == '-'){
				for(int j = i - k + 1 ; j <= i ; ++j){
					str[j] = (str[j] == '+') ? '-' : '+';
				}
				++ans;
			}
		}
		for(int i = 1 ; i < k ; ++i){
			if(str[i] == '-'){
				ans = inf;
			}
		}
		if(ans >= inf){
			printf("IMPOSSIBLE\n");
		}
		else{
			printf("%d\n" , ans);
		}
	}
}