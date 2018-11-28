#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;

int n, x, s[10101];
bool used[10101];
int main(){
	freopen("test.in", "r", stdin);
	freopen("1.out", "w", stdout);
	int cases; scanf("%d",&cases);
	for (int it=1;it<=cases;it++){
		printf("Case #%d: ", it);
		scanf("%d%d",&n,&x);
		for (int i=0;i<n;i++) scanf("%d",&s[i]);
		sort(s, s+n);
		memset(used, false, sizeof(used));
		int cnt = 0;
		for (int i=n-1;i>=0;i--) if (!used[i]){
			used[i] = true;
			cnt++;
			int found = -1;
			for (int j=i-1;j>=0;j--) if (!used[j] && s[j] + s[i] <= x){
				found = j;
				break;
			}
			if (found != -1) used[found] = true;
		}
		printf("%d\n",cnt);
	}
	return 0;
}