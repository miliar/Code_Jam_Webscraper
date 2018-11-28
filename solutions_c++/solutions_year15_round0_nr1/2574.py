#include<stdio.h>
int res[100000],t;
void output()
{int i;
 for(i=0;i<t;i++)
 printf("case #%d: %d\n",i+1,res[i]);
}
int main()
{char a[10000];
 int ova,i,n,j,count;
 scanf("%d",&t);
 for(i=0;i<t;i++)
{count=0;
 scanf("%d",&n);
 scanf("%s",a);
ova=a[0]-48;

for(j=1;j<=n;j++)
{
 if((ova+count)<j)
  count++;
 ova+=a[j]-48;
}
res[i]=count;
}
output();
}
