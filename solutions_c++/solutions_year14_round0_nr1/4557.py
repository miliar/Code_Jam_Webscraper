
#include<cstdio>
#include<algorithm>
using namespace std;
int cnt[17];
int main() {
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A.txt","w",stdout);
	int TT;
	scanf("%d",&TT);
	for(int TTT=1;TTT<=TT;TTT++) {
		fill(cnt,cnt+17,0);
		for(int k=0;k<=1;k++) {
			int row,t;
			scanf("%d",&row);
			for(int i=1;i<=4;i++) {
				for(int j=0;j<4;j++) {
					scanf("%d",&t);
					if(i==row) cnt[t]++;
				}
			}
		}
		int ans=-1,num=0;
		for(int i=1;i<=16;i++) if(cnt[i]==2) {
			num++;
			ans=i;
		}
		printf("Case #%d: ",TTT);
		if(num==1) printf("%d\n",ans);
		else if(num>1) printf("Bad magician!\n");
		else if(num==0) printf("Volunteer cheated!\n");
	}
	return 0;
}

