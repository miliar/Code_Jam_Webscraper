#include<stdio.h>

int main()
{int T;
scanf("%d",&T);
for(int i=0;i<T;i++)
{int N,flag=1,frog=0,S[10],a,b;
scanf("%d",&N);
if(N==0)
{
frog=11;
}
while(frog<10)
{
a=N;
a=a*flag;
while(a)
{
int flag1=1;
b=a%10;
for(int j=0;j<frog;j++)
{if(b==S[j])
{flag1=0;
}}
if(flag1==1)
{S[frog]=b;
frog++;
}
a=a/10;
}
flag++;
}
if(frog==11)
{printf("CASE #%d: INSOMNIA \n",i+1);
}
else
{printf("CASE #%d: %d \n",i+1,N*(flag-1));
}
}
return 0;
}
