#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int t, n, s, l[10005], ans;
bool used[10005];

int main(){
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	scanf("%d", &t);
	for(int k = 1; k <= t; ++k){
		scanf("%d%d", &n, &s);
		ans = 0;
		memset(used, false, sizeof used);
		for(int a = 0; a < n; ++a) scanf("%d", &l[a]);
		sort(l, l+n);
		int pos = n-1;
		for(int a = 0; a < n; ++a){
			if(!used[a]){
				used[a] = true;
				int temp = l[a];
				while(pos > a){
					if(temp + l[pos] <= s){
						used[pos] = true;
						--pos;
						break;
					}
					--pos;
				}
				++ans;
			}
		}
		printf("Case #%d: %d\n", k, ans);
	}
	return 0;
}
