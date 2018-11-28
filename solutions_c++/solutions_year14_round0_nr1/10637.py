#include <stdio.h>
#include <iostream>
using namespace std;

main(){
	FILE *fp,*fp1;
	fp=fopen("A-small-attempt1.in","r");
	fp1=fopen("output.txt","w");
	int t,a[4][4],b[4][4],ans1,ans2,cnt=0,i,j,n=1,index;
	fscanf(fp,"%d",&t);
	while(t--){
		fscanf(fp,"%d",&ans1);
		
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				fscanf(fp,"%d",&a[i][j]);
				
		fscanf(fp,"%d",&ans2);
		
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				fscanf(fp,"%d",&b[i][j]);
		
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				if(a[ans1-1][i]==b[ans2-1][j]){
					cnt++;
					if(cnt==1)
						index=i;
				}
		
		if(cnt==1)
			fprintf(fp1,"Case #%d: %d\n",n,a[ans1-1][index]);
		else if(cnt>1)	
			fprintf(fp1,"Case #%d: Bad magician!\n",n);
		else
			fprintf(fp1,"Case #%d: Volunteer cheated!\n",n);
	
		cnt=0;
		n++;
	}
}