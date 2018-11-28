#include <cstdio>

using namespace std;

char s[1008];

int main(){
	int t, n, cas = 1;

	//freopen("in.txt", "r", stdin);
	//freopen("A-large.in", "r", stdin);
	//freopen("out.txt", "w", stdout);
	scanf("%d", &t);
	while(t--){
		scanf("%d%s", &n, s);
		int now = 0, res = 0;
		for(int i = 0; i <= n; i++){
			int tp = s[i] - '0';
			if(now >= i) now += tp;
			else{
				res += i - now;
				now = i + tp;
			}
		}
		printf("Case #%d: %d\n", cas++, res);
	}

	return 0;
}
