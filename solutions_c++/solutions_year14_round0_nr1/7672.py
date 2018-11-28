#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
FILE *fin = fopen("A-small-attempt2.in","r");
FILE *fout = fopen("output.out","w");
int t,n1,n2,a1[5][5],a2[5][5],i,j,k,x,sum = 0;
fscanf(fin,"%d",&t);

for(i=0;i<t;i++)
{
fscanf(fin,"%d",&n1);
for(j=1;j<5;j++) for(k=1;k<5;k++) fscanf(fin,"%d",&a1[j][k]);
fscanf(fin,"%d",&n2);
for(j=1;j<5;j++) for(k=1;k<5;k++) fscanf(fin,"%d",&a2[j][k]);

for(j=1;j<5;j++)
{

for(k=1;k<5;k++)
{ if(a2[n2][k] == a1[n1][j]) {sum++; x = a2[n2][k]; } } 


}

if(sum == 1) fprintf(fout,"Case #%d: %d\n",i+1,x);
else if(sum == 2 || sum ==  3 || sum == 4) fprintf(fout,"Case #%d: Bad magician!\n",i+1);
else if(sum == 0) fprintf(fout,"Case #%d: Volunteer cheated!\n",i+1);


sum = 0;
}
return 0;
}
