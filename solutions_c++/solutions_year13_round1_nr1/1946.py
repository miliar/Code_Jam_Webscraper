#include<stdio.h>
#include<stdlib.h>
#include<math.h>
void main()
{
int r,t,i,j=1,n,s,count=0;
FILE* read;
FILE* w;
read=NULL;
w=NULL;
read=fopen("E:\\file.txt","r");
w=fopen("E:\\futput.txt","w");
fscanf(read,"%d",&n);
while(j<=n)
{
  fscanf(read,"%d%d",&r,&t);
  s=((r+1)*(r+1))-(r*r);
  while(s<=t)
  {
	count++;
	t=t-s;
	r=r+2;
	s=((r+1)*(r+1))-(r*r);
  }
  fprintf(w,"Case #%d: %d\n",j,count);
  count=0;
  j++;
}
fclose(read);
fclose(w);
}
