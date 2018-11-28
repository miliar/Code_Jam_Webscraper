#include<bits/stdc++.h>
using namespace std;
#define FOR(i, a, b) for(int i=a;i<b;i++) 
char s[10004], a[10004];
int arr[10004], till[10004], sign[10004];
int op[4][4] = {0, 1, 2 ,3, 1, 0, 3, 2, 2, 3, 0, 1, 3, 2, 1, 0};
int si[4][4] = {1, 1, 1, 1, 1, -1, 1, -1, 1, -1, -1, 1, 1, 1, -1, -1};
int main() {
	int t, l, x, n;	
	bool np;
	scanf("%d",&t);
	FOR(T, 0, t) {
		scanf("%d %d",&l, &x);
		scanf("%s",s);
		n = l * x;
		FOR(i, 0, n) a[i] = s[i%l];
		FOR(i, 0, n) {
			if(a[i] == 'i') arr[i] = 1;
			else if(a[i] == 'j') arr[i] = 2;
			else if(a[i] == 'k') arr[i] = 3;
		}
		till[0] = arr[0];
		sign[0] = 1;
		FOR(i, 1, n) {
			till[i] = op[till[i-1]][arr[i]];
			sign[i] = sign[i-1] * (si[till[i-1]][arr[i]]);
		}
		np = false;
		if(sign[n-1] == -1 && till[n-1] == 0) {
			FOR(i, 0, n) {
				if(sign[i] == 1 && till[i] == 1) {
					FOR(j, i+1, n) {
						if(sign[j] == 1 && till[j] == 3) {
							np = true;
							break;
						}
					}
					break;
				}
			}	
		}
		printf("Case #%d: ",T+1);
		if(np) puts("YES");
		else puts("NO");
	}
	return 0;
}
