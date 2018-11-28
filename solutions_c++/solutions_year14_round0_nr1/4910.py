#include<stdio.h>
void main()
{
 FILE *f1, *f2;
 f1 = fopen("A.in","r");
 f2 = fopen("Aoutput.txt","w");
 int t,a1,a2;
 int a[4][4],b[4][4];
 int count,num;
 fscanf(f1,"%d",&t);
 for(int i=0;i<t;i++)
 {
  count = 0;
  fscanf(f1,"%d",&a1);
  for(int j=0;j<4;j++)
   for(int k=0;k<4;k++)
    fscanf(f1,"%d",&a[j][k]);
  fscanf(f1,"%d",&a2);
  for(j=0;j<4;j++)
   for(k=0;k<4;k++)
    fscanf(f1,"%d",&b[j][k]);

  for(j=0;j<4;j++)
  {
   for(k=0;k<4;k++)
   {
    if(a[a1-1][j]==b[a2-1][k])
    {
      count++;
      num=a[a1-1][j];
    }
   }
  }
  if(count==0)
  {
   fprintf(f2,"Case #%d: Volunteer cheated!\n",i+1);
  }
  if(count==1)
  {
   fprintf(f2,"Case #%d: %d\n",i+1,num);
  }
  if(count>1)
  {
   fprintf(f2,"Case #%d: Bad magician!\n",i+1);
  }
 }
 fclose(f1);
 fclose(f2);
}