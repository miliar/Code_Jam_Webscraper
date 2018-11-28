#include<stdio.h>
#include<stdlib.h>
long long pow(long long z,long long a)
{
long long p,m;
m=a;p=1;
while(m)
{
while((m%2)==0)
{
m=m/2;
z=(z*z);
}
m=m-1;
p=(p*z);
}
return p;
}

int main()
{
long long t,n,i,j,nd,a,ans,o,p,ten,m;
int occur[10],ndig[20];
FILE *fptr,*op;
fptr=fopen("F:/a.txt","r");
op=fopen("F:\co.txt","w");
op=fopen("F:\co.txt","a");
fscanf(fptr,"%lld",&t);
for(j=1;j<=t;j++)
{nd=0;ans=-1;o=0;
for(i=0;i<10;i++)
    occur[i]=0;
for(i=0;i<20;i++)
    ndig[i]=0;
 fscanf(fptr,"%lld",&n);
 if(n==0)
     fprintf(op,"Case #%lld: INSOMNIA\n",j);
 else
 {
     a=n;
 while(a>0)
 {
     nd++;
     p=a%10;
     if(occur[p]==0)
       {
        ++o;
     occur[p]=1;}
     a/=10;
 }
 ndig[nd]=1;
 m=pow(10,nd);ten=nd;
 for(i=2;i<=m;i++)
 {
     a=i*n;nd=0;
      while(a>0)
 {
     nd++;
     p=a%10;
     if(occur[p]==0)
         {
        ++o;
     occur[p]=1;}
     a/=10;
 }
 ndig[nd]=i;
 if(o==10)
 {
     ans=i*n;break;
 }
 }
 for(--i;o!=10;i++)
 {
     if(i==m)
        {i+=ndig[ten];m*=10;ten++;}
         a=n*i;nd=0;
      while(a>0)
 {
     nd++;
     p=a%10;
     if(occur[p]==0)
      {
        ++o;
     occur[p]=1;
      }
     a/=10;
 }
 ndig[nd]=i;
 if(o==10)
 {
     ans=i*n;break;
 }
 }
 fprintf(op,"Case #%lld: %lld\n",j,ans);
}
}
return 0;
}

