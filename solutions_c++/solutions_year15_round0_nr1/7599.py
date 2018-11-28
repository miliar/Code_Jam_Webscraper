#include <cstdio>
#include <iostream>

using namespace std;

const int MAX_N = 1100;

int tests;
int sMax;
char temp[MAX_N];
int cnt[MAX_N];

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++){
		scanf("%d %s", &sMax, temp);
		for (int i = 0; i <= sMax; i++){
			cnt[i] = temp[i] - '0';
		}
		int res = 0;
		int cur = cnt[0];
		for (int i = 1; i <= sMax; i++){
			if (cnt[i] > 0){
				if (cur < i){
					res += i - cur;
					cur = i;
				}
				cur += cnt[i];
			}			
		}
		printf("Case #%d: %d\n", test, res);   	
	}
	return 0;              
}