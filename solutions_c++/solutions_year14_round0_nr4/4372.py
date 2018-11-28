#include <iostream>
#include <fstream>
#include <algorithm>
#include <stdio.h>
using namespace std;  
double Naomi [1001], Ken[1001];
int used[1001];
int test(int n, bool cheat) {
	int i, j, score = 0;
	if (!cheat) score = n;
	memset(used, 0, sizeof(used));
	for (i=0; i<n; ++i)
		for (j=0; j<n; ++j)
			if (used[j]==0){
				if (cheat) {
					if (Naomi[j]>Ken[i]) {used[j]=1;++score;break;}
				} else {
					if (Ken[j]>Naomi[i]) {used[j]=1;--score;break;}
				}
			}
	return score;
}
int main() {  
    freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
    int cas, t, i, j, k, n;
    scanf("%d", &t);
	for (cas=1; cas<=t; ++cas) {
        scanf("%d", &n);
		for (i=0; i<n; ++i) scanf("%lf", &Naomi[i]);
		sort(Naomi, Naomi+n);
		for (i=0; i<n; ++i) scanf("%lf", &Ken[i]);
		sort(Ken, Ken+n);		
        printf("Case #%d: %d %d\n", cas, test(n, true), test(n, false));  
	}
	return 0;
}  
