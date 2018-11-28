#include<stdio.h>
#include<conio.h>
int main()
{
FILE *fp,*fp1;
int a[4][4],b[4][4],i=0,j,k,T,n1,n2,flag=0,m;
fp=fopen("code.in","r");
fp1=fopen("code1.txt","w");
fscanf(fp,"%d",&T);
for(i=0;i<T;i++)
    {
    fscanf(fp,"%d",&n1);
    for(j=0;j<4;j++)
	{
	 for(k=0;k<4;k++)
	   {
	     fscanf(fp,"%d",&a[j][k]);
	   }
	}
    fscanf(fp,"%d",&n2);
    for(j=0;j<4;j++)
	{
	 for(k=0;k<4;k++)
	     fscanf(fp,"%d",&b[j][k]);
	}
	flag=0;
   for(j=0;j<4;j++)
       {
	for(k=0;k<4;k++)
	    {
	    if(a[n1-1][j]==b[n2-1][k])
	      {
	       flag++;
	       m=j;
	      }
	    }
       }
      fprintf(fp1,"Case #%d: ",i+1);
     if(flag==0)
	fprintf(fp1,"Volunteer cheated!\n");
     else if(flag==1)
	fprintf(fp1,"%d\n",a[n1-1][m]);
    else if(flag>1)
       fprintf(fp1,"Bad magician!\n");
    }
    fclose(fp);
    fclose(fp1);
    return 0;
}