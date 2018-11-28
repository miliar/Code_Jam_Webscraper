#include <stdio.h>
#include <algorithm>

using namespace std;

int T,TT;
int a1,a2,t1[4][4],t2[4][4];
int cnt,p;

int main(void) {
	int i,j;
	scanf("%d",&TT);
	while(TT--){
		scanf("%d",&a1);
		for(i=0;i<4;i++)for(j=0;j<4;j++)
			scanf("%d",&t1[i][j]);
		scanf("%d",&a2);
		for(i=0;i<4;i++)for(j=0;j<4;j++)
			scanf("%d",&t2[i][j]);
		a1--;a2--;
		sort(t1[a1],t1[a1]+4);
		sort(t2[a2],t2[a2]+4);
		for(i=j=cnt=0;i<4&&j<4;){
			if(t1[a1][i]<t2[a2][j])i++;
			else if (t1[a1][i]>t2[a2][j])j++;
			else{
				p=i;
				cnt++;
				i++;
				j++;
			}
		}
		printf("Case #%d: ",++T);
		if(cnt==0)
			printf("Volunteer cheated!\n");
		else if (cnt==1)
			printf("%d\n",t1[a1][p]);
		else
			printf("Bad magician!\n");
	}
	return 0;
}
