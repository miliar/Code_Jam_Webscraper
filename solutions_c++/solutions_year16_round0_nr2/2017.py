#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

int T;
char ch[200];
int f[200][2];

int main() {
	freopen("2B.in","r",stdin);
	freopen("2B.out","w",stdout);
	scanf("%d",&T);
	for (int kase = 1;kase <= T; kase++) {
		scanf("%s",ch);
		int l = strlen(ch);
		if (ch[0] == '+') f[0][1] = 0,f[0][0] = 1;
		else f[0][0] = 0,f[0][1] = 1;
 		for (int i = 1;i < l; i++) {
 			int t = ch[i] == '+';
 			if (t == 0) {
 				f[i][0] = min(f[i-1][0],f[i-1][1]+1);
 				f[i][1] = min(f[i-1][0]+1,f[i-1][1]+2);
 			}
 			else {
 				f[i][0] = min(f[i-1][1]+1,f[i-1][0]+2);
 				f[i][1] = min(f[i-1][1],f[i-1][0]+1);
 			}
		}
		printf("Case #%d: %d\n",kase,f[l-1][1]);
	}
	return 0;
}