
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define MAX 1010

char s[MAX];
int t, n, tot, res;

int main(){
    freopen("A-large.in", "rt", stdin);
    freopen("A-large.ou", "wt", stdout);
	scanf("%d", &t);
	for (int cs = 1; cs <= t; cs++){
		tot = res = 0;
		scanf("%d%s", &n, s);
		for (int i = 0;i <= n; i++){
			if (tot < i){
				res += (i - tot);
				tot = i;
			}
			tot += s[i] - '0';
		}
		printf("Case #%d: %d\n", cs, res);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
