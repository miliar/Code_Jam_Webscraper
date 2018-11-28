#include<iostream>
#include<stdio.h>

using namespace std;
double a[1050],b[1050];
void sort(int m)
{
int i,j;
double t;
for(i=0;i<m-1;i++)
for(j=0;j<m-i-1;j++)
{
if(a[j]>a[j+1])
{
t=a[j];
a[j]=a[j+1];
a[j+1]=t;
}
if(b[j]>b[j+1])
{
t=b[j];
b[j]=b[j+1];
b[j+1]=t;
}

}
}
int main(){
int n,i,m,ans,dans,j,k;
//FILE *fp=fopen("attempt1.in","r");
//FILE *fpo=fopen("out.txt","w");
cin>>n;
//fscanf(fp,"%d",&n);
for(i=1;i<=n;i++)
{
//fscanf(fp,"%d",&a);
cin>>m;

for(j=0;j<m;j++)
cin>>a[j];

for(k=0;k<m;k++)
cin>>b[k];

sort(m);
dans=0;

for(k=0,j=0;k<m;k++)
if(a[k]>b[j])
{
dans++;
j++;
}


ans=0;
for(k=0,j=0;k<m;k++)
{
while(j<m)
if(a[k]<b[j++])
{
ans++;
break;
}
if(j==m)
break;
}

//fprintf(fpo,"Case #%d: Bad magician!\n",i+1);
printf("Case #%d: %d %d\n",i,dans,m-ans);
}
}

