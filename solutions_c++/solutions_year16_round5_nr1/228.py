#include <cstdio>
#include <cstring>
using namespace std;
#define N 22222
int n;
char s[N];
int ex[N], nx[N];

int main(){
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int _, __ = 0;
	scanf("%d", &_);
	while (_--){
		printf("Case #%d: ", ++ __);
		scanf("%s", s + 1);
		n = strlen(s + 1);
		for (int i = 0; i <= n + 1; ++ i){
			ex[i] = i - 1;
			nx[i] = i + 1;
		}
		int len = n;
		for (int i = 1; i <= n; i = nx[i]){
			while (i > 0 && nx[i] <= n && s[i] == s[nx[i]]){
				len -= 2;
				nx[ex[i]] = nx[nx[i]];
				ex[nx[nx[i]]] = ex[i];
				i = ex[i];
			}
		}
		printf("%d\n", (n - len) * 5 + (len / 2) * 5);
	}
	return 0;
}