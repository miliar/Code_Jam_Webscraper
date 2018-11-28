#include<stdio.h>
#include<conio.h>
#include<math.h>

int palindrome(int n)
{
if(n==int(n))
{
int i,num,b=0;
num=int(n);
for(i=0;num!=0;i++)
{b=b*10+num%10;
num=num/10;
}
if(b==n)
return 1;
else
return 0;
}
}

int main()
{freopen("input.in","r",stdin);
freopen("output.out","w",stdout);
    int c,k;
scanf("%d",&c);
for(k=1;k<=c;k++)
{
  long long int a,b,i,count=0;
  float rem;
  scanf("%lld %lld",&a,&b);
  for(i=a;i<=b;i++)
  if(palindrome(i))
  {if(sqrt(i)==int(sqrt(i)))
     count=count+palindrome(int(sqrt(i)));}
  printf("Case #%d: %d\n",k,count);
}
getch();
return 0;
}

