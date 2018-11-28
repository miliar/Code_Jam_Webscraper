#include <iostream>
#include <cstdio>
using namespace std;

int main() 
{
	int T,t,ar1[5][5],ar2[5][5],ans1,ans2,i,j,found_count;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%d\n",&ans1);
		for(i=1;i<=4;i++) for(j=1;j<=4;j++) scanf("%d",&ar1[i][j]);
		scanf("%d\n",&ans2);
		for(i=1;i<=4;i++) for(j=1;j<=4;j++) scanf("%d",&ar2[i][j]);
		
		
		found_count=0;
		for(i=1;i<=4;i++) for(j=1;j<4;j++) if(ar1[ans1][i]==ar2[ans2][j]) found_count++;
		
		if(found_count>1) printf("Case #%d: Bad magician!\n",t);
		else if(found_count==0) printf("Case #%d: Volunteer cheated!\n",t);
		else for(i=1;i<=4;i++) for(j=1;j<4;j++) if(ar1[ans1][i]==ar2[ans2][j]) printf("Case #%d: %d\n",t,ar1[ans1][i]);
		
	}
	
	return 0;
	
}