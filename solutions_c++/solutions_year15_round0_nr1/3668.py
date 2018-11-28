#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
	int q;
	scanf("%d", &q);
	for(int i=1;i<=q;++i){
		int n;
		scanf("%d", &n);
		char t[1005];
		scanf("%s", t);
		int mx=0, ile=0;
		for(int j=0;j<=n;++j){
			mx=max(mx,j-ile);
			ile+=t[j]-'0';
		}
		printf("Case #%d: %d\n", i, mx);
	}
	return 0;
}
