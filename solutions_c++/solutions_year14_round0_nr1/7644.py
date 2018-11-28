#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	FILE *fp;
	int a[5],b[5];
	int no;
	int tt,t,ra,rb,i,j;
	fp = fopen("out","w");
	scanf("%d",&t);
	for(tt=1;tt<=t;tt++){
		scanf("%d",&ra);
		for(i=1;i<=4;i++){
			for(j=0;j<4;j++){
				if(i==ra){					
					scanf("%d",&a[j]);					
				}
					
				else
					scanf("%d",&no);
			}
		}
	//	for(i=0;i<4;i++)
	//	printf("(%d)",a[i]);
		scanf("%d",&rb);
		for(i=1;i<=4;i++){
			for(j=0;j<4;j++){
				if(i==rb)
					scanf("%d",&b[j]);
				else
					scanf("%d",&no);
			}
		}
		
		int count=0;
		int number;		
		for(i=0;i<4;i++){
			for(j=0;j<=4;j++){
				if(a[i]==b[j]){
					count++;
					number=a[i];
				}
			}
		}
		
		fprintf(fp,"Case #%d: ",tt);
		if(count==0)
		fprintf(fp,"Volunteer cheated!\n");
		else if(count==1)
		fprintf(fp,"%d\n",number);
		else
		fprintf(fp,"Bad magician!\n");
			
	}
	fclose(fp);
	return 0;
} 
