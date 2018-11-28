
#include <iostream>
#include <stdio.h>
#include <string.h>
#include <fstream>
#include <math.h>
#include <stdlib.h>
using namespace std;

int check(int i,int f)
{
  char c [50];
  int l;
  
  l=sprintf (c,"%d",i);
  l=l-1;
int j;
  
for(j=0;j<=l;j++)
{
if(c[j]!=c[l-j]){ return 0;}

}

if(f==0)
{
j=sqrt(i);
if(j*j==i)
return check(j,1);
else
return 0;
}

return 1;




  return 0;
}



int main()
{


int T;

int i=0,j=0,k=0;
int l,h;
int c=0;

FILE *fp;
FILE *out;

fp=fopen("a.in","r");

ofstream outfile("k.txt");

fscanf(fp,"%d\n",&T);


for(i=0;i<T;i++){
c=0;
fscanf(fp,"%d\t",&l);
fscanf(fp,"%d\n",&h);
j=0;
for(k=l;k<=h;k++){

j=check(k,0);

c=c+j;
}

//printf("Case #%d: %d\n",i,c);

outfile <<"Case #"<<i+1<<": "<<c<<endl;



}


fclose(fp);


return 0;
}
