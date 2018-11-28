//by Vandit Jain, MNNIT ALLAHABAD
#include<stdio.h>
#define loop(i,n) for(int i=0;i<n;i++)
main(){
	int t,a1,a2;
	int a[4][4],b[4][4];
	scanf("%d",&t);
	int x=0;
	while(t--){
		scanf("%d",&a1);
		a1--;
		loop(i,4)
			loop(j,4)
				scanf("%d",&a[i][j]);
		scanf("%d",&a2);
		a2--;
		loop(i,4)
			loop(j,4)
				scanf("%d",&b[i][j]);
		int c=0,no;
		loop(i,4)
			loop(j,4)
				if(a[a1][i]==b[a2][j]){
					c++;
					no=a[a1][i];
				}
		x++;
		if(c==1)
			printf("Case #%d: %d\n",x,no);
		else if(c==0)
			printf("Case #%d: Volunteer cheated!\n",x);
		else printf("Case #%d: Bad magician!\n",x);
	}			
}