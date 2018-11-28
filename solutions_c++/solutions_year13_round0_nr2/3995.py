#include<stdio.h>
int main()
{
int a[101][101],i,j,flag,max,t,n,m,min[101],k,l,flag1;
FILE *fp1,*fp2;
fp1=fopen("B-large.in","r");
fp2=fopen("output.txt","w");
fscanf(fp1,"%d",&t);
l=1;
while(t--)
{
fscanf(fp1,"%d%d",&n,&m);

for(i=0;i<n;i++)
{
for(j=0;j<m;j++)
{
fscanf(fp1,"%d",&a[i][j]);

}
}

flag=flag1=0;
for(i=0;i<n;i++)
{
for(j=0;j<m;j++)
{

for(k=0;k<m;k++)
{
if(a[i][k]>a[i][j])
flag=1;
}
for(k=0;k<n;k++)
{
if(a[k][j]>a[i][j])
flag1=1;
}
if(flag==1 && flag1==1)
{
break;
}
else
flag=flag1=0;
}

if(flag==1 && flag1==1)
break;
}
if(flag==1 && flag1==1)
fprintf(fp2,"Case #%d: NO\n",l);
else if(flag==0 || flag1==0)
fprintf(fp2,"Case #%d: YES\n",l);
l++;
}
return 0;
}
