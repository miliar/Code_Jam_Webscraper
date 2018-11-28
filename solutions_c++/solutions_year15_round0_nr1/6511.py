#include <stdio.h>
#include <algorithm>
#include <queue>

struct pt {
	int x,y;
};

using namespace std;

int main() {
	freopen("ova.out","w",stdout);
	int t,n,j,i;
	char c;
	scanf("%d\n",&t);
	for (i=0;i<t;i++) {
		scanf("%d ",&n);
		queue <pt> q;
		printf("Case #%d: ",i+1);
		for (j=0;j<=n;j++) {
			scanf("%c",&c);
			c-='0';
			pt kek;
			kek.x=j;
			kek.y=c;
			q.push(kek);
		}
		int num=0,ans=0;
		while (!q.empty()) {
			ans+=max(q.front().x-num,0);
			num+=max(q.front().x-num,0);
			num+=q.front().y;
			q.pop();
		}
		printf("%d\n",ans);
	}
}