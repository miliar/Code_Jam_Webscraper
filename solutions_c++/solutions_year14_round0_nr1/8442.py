#include <stdio.h>
using namespace std;

main(){
	int tests;
	scanf("%d",&tests);
	for(int casenum=1;casenum<=tests;casenum++){
		printf("Case #%d: ",casenum);
		int chk[17]={};
		for(int t=0;t<2;t++){
			int r;
			scanf("%d",&r);
			for(int i=0;i<16;i++){
				int tmp;
				scanf("%d",&tmp);
				if(i/4==r-1)chk[tmp]++;
			}
		}
		int ans;
		int cnt=0;
		for(int i=1;i<=16;i++)if(chk[i]==2){ans=i;cnt++;}
		if(cnt==0)puts("Volunteer cheated!");
		else if(cnt>=2)puts("Bad magician!");
		else printf("%d\n",ans);
	}
}