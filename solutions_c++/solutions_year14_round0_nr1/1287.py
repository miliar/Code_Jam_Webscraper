
#include <cstdio>
#include <cstring>
using namespace std;

int T;
int ra,rb;
int a[17];
int b[17];

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for (int ww=1;ww<=T;ww++) {
		printf("Case #%d: ",ww);
		int ans=-1,cnt=0,tmp;
		scanf("%d",&ra);
		for (int i=1;i<=4;i++) {
			for (int j=1;j<=4;j++) {
				scanf("%d",&tmp);
				a[tmp]=i;
			}
		}
		scanf("%d",&rb);
		for (int i=1;i<=4;i++) {
			for (int j=1;j<=4;j++) {
				scanf("%d",&tmp);
				b[tmp]=i;
			}
		}
		for (int i=1;i<=16;i++) {
			if (a[i]==ra && b[i]==rb) {
				cnt++;
				ans=i;
			}
		}
		if (cnt==1) printf("%d\n",ans);
		if (cnt>1) printf("Bad magician!\n");
		if (cnt<1) printf("Volunteer cheated!\n");
	}
	return 0;
}
