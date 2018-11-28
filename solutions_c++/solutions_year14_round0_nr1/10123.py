#include<iostream>
using namespace std;
int main()
{
FILE *f1,*f2;
int n,ans1,ans2,ar1[4][4],ar2[4][4];
f1=fopen("A-small-attempt0.in","r");
f2=fopen("output.txt","w");
fscanf(f1,"%d",&n);
for(int i=0;i<n;i++)
{
int count=0,p[4],k=0;
fscanf(f1,"%d",&ans1);
for(int i=0;i<4;i++)
for(int j=0;j<4;j++)
fscanf(f1,"%d",&ar1[i][j]);
fscanf(f1,"%d",&ans2);
for(int i=0;i<4;i++)
for(int j=0;j<4;j++)
fscanf(f1,"%d",&ar2[i][j]);
for(int a=0;a<4;a++)
{
for(int b=0;b<4;b++)
{
if(ar1[ans1-1][a]==ar2[ans2-1][b])
{
++count;
p[k]=ar1[ans1-1][a];
++k;
}
}}
if(count==1)
fprintf(f2,"Case #%d: %d\n",i+1,p[0]);
else if(count>1)
fprintf(f2,"Case #%d: Bad magician!\n",i+1);
else if(count==0)
fprintf(f2,"Case #%d: Volunteer cheated!\n",i+1);
}
fclose(f1);
fclose(f2);
return 0;
}
