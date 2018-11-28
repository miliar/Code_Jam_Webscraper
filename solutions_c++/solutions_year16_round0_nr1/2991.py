#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;


int doit(int x) {
	bool a[10] = {false};
	int  count  = 0, y=x;
	while(1) {
		int tmp = y;
		while(tmp) {
			if(!a[tmp%10]) {
				a[tmp%10] = true;
				if(++count == 10) return y;
			}
			tmp /= 10;
		}
		y+=x;
	}
	return 0;
}

int main() {

	// freopen("A-small-attempt0.in","r",stdin);
	// freopen("A-small-attempt0.out","w",stdout);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int T, cas = 0;
	scanf("%d",&T);
	while(T--) {
		int x;
		scanf("%d",&x);
		printf("Case #%d: ",++cas);
		if(x==0) puts("INSOMNIA");
		else printf("%d\n",doit(x));
	}
	return 0;
} 