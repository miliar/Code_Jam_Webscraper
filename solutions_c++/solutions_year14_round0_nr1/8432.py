#include <bits/stdc++.h>

using namespace std;

int TC,a,jml[20],x,ans,pos,caseNo;

int main() {
	scanf("%d",&TC);
	while(TC--) {
		for(int i = 1; i<=16; i++)
			jml[i] = 0;
		scanf("%d",&a);
		for(int i = 1; i<=4; i++)
			for(int j = 1; j<=4; j++) {
				scanf("%d",&x);
				if(i == a)
					jml[x]++;
			}
		scanf("%d",&a);
		for(int i = 1; i<=4; i++)
			for(int j = 1; j<=4; j++) {
				scanf("%d",&x);
				if(i == a)
					jml[x]++;
			}
		ans = 0;
		pos = -1;
		for(int i = 1; i<=16; i++) if(jml[i] == 2) {
			ans++;
			pos = i;
		}
		printf("Case #%d: ",++caseNo);
		if(ans == 0)
			puts("Volunteer cheated!");
		else if(ans == 1)
			printf("%d\n",pos);
		else
			puts("Bad magician!");
	}
}