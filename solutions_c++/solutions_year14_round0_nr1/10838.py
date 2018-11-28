#include<stdio.h>
#include<conio.h>

void main()
{
 FILE *fpr,*fpw;
 int i,j,k,answer1,answer2,number;
 int array1[4][4],array2[4][4],flag=0;

 fpr=fopen("input.txt","r");
 fpw=fopen("output.txt","w");

 for(i=1;i<=100;i++)
 {
  fscanf(fpr,"%d",&answer1);   //first answer.
  --answer1;
  for(j=0;j<4;j++)
  {
   for(k=0;k<4;k++)
   {
    fscanf(fpr,"%d",&array1[j][k]);      //first array
   }
  }

  fscanf(fpr,"%d",&answer2);	  //second answer
  --answer2;
  for(j=0;j<4;j++)
  {
   for(k=0;k<4;k++)
   {
    fscanf(fpr,"%d",&array2[j][k]);      //second array
   }
  }
   for(j=0;j<4;j++)                  //awesome comparison logic
   {
    for(k=0;k<4;k++)
    {
     if(array1[answer1][j]==array2[answer2][k])
     {
      number=array1[answer1][j];
      flag++;
     }
    }
   }
  if(flag==0)
	fprintf(fpw,"Case #%d: Volunteer cheated!\n",i);
  else if(flag==1)
       fprintf(fpw,"Case #%d: %d\n",i,number);
  else
	fprintf(fpw,"Case #%d: Bad magician!\n",i);
   flag=0;
 }
 fclose(fpr);
 fclose(fpw);
}