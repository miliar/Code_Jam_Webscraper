#include<stdio.h>
#include<stdlib.h>
int main(void){
	int t,hh;
	freopen("2014Q_pA.in","r",stdin);
	freopen("2014Q_pA.txt","w",stdout);
	scanf("%d",&t); 
	for(hh=1;hh<=t;hh++){
		int r1,r2,i,j;
		int m1[6][6],m2[6][6];
		int u[17];
		for(i=1;i<=16;i++)
		  u[i]=0;
		scanf("%d",&r1);
		for(i=1;i<=4;i++)
		  for(j=1;j<=4;j++){
		     scanf("%d",&m1[i][j]);
		     if(i==r1)
		       u[m1[i][j]]++;
		  }
		scanf("%d",&r2);
		for(i=1;i<=4;i++)
		  for(j=1;j<=4;j++){
		    scanf("%d",&m2[i][j]);
		    if(i==r2)
		      u[m2[i][j]]++; 
		  }
		int ans=-1,ff=0;
		for(i=1;i<=16;i++){
		  if(u[i]==2&&ans!=-1) ff=1; 
		  if(u[i]==2&&ans==-1) ans=i;
	    }
	    if(ans==-1) printf("Case #%d: Volunteer cheated!\n",hh);
	    else if(ff==1) printf("Case #%d: Bad magician!\n",hh);
	    else printf("Case #%d: %d\n",hh,ans);
		
	}
	return 0;
} 
