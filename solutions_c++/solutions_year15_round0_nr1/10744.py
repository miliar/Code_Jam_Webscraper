#include<stdio.h>
#include<conio.h>


int main(void)
{
FILE *file1,*file2;

int T,Smax,counter,friends,i,j,k;

counter=0;
friends=0;
i=0;j=0;

clrscr();

file1=fopen("A-small1.in","r");
file2=fopen("outA.in","w");
if(file1==NULL)
  {
   perror("file open error");
   return 0;
   }
if(file2==NULL)
  {
   printf("file open error");
   return 0;
   }

//T=getc(file1);

fscanf(file1,"%d",&T);

printf("test cases:%d",T);
for(j=T;j>0;j--)
{
 // Smax=getw(file1);
  fscanf(file1,"%1d",&Smax);
  printf("smax:%d\n",Smax);
  for(i=0;i<=Smax;i++)
  {   fscanf(file1,"%1d",&k);
  printf("%d",k);
   // k=getw(file1);
    counter=counter+k;
    printf("counter:%d",counter);
	if( (counter+friends)<=i)
	{
	  friends++;
	  printf("friends:%d",friends);
	}
  }
  fprintf(file2,"Case #%d: %d\n",T-j+1,friends);
  counter=0; friends=0;
}
fclose(file1);
fclose(file2);
return 0;
}