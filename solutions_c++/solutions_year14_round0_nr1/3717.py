#include<stdio.h>
#include<set>
#include<algorithm>
#include<stdlib.h>

using namespace std;
int main()
{
int t,k=1;
int i,a,b,c,d,num,ans,val1,val2;
scanf("%d",&t);
while(k<=t)
{

set<int> s;

scanf("%d",&val1);
for(i=1;i<=4;i++)
{
scanf("%d %d %d %d",&a,&b,&c,&d);
if(i==val1)
{
s.insert(a);
s.insert(b);
s.insert(c);
s.insert(d);
}
}
//printf("before:%d %d %d %d\n",a,b,c,d);

num=0;ans=0;
scanf("%d",&val2);
for(i=1;i<=4;i++)
{
scanf("%d %d %d %d",&a,&b,&c,&d);
//printf("after: %d %d %d %d\n",a,b,c,d);
if(i==val2)
{
if(s.count(a)==1)
  {num++; ans=a;/*printf("into a\n");*/}
  
if(s.count(b)==1)
  {num++; ans=b;/*printf("into b\n");*/}

if(s.count(c)==1)
  {num++; ans=c; /*printf("into c\n");*/}

if(s.count(d)==1)
  {num++; ans=d; /*printf("into d\n");*/}

}
}
//final output
if(num==1)
printf("Case #%d: %d\n",k,ans);
else
if(num>1)
printf("Case #%d: Bad magician!\n",k);
else if(num==0)
printf("Case #%d: Volunteer cheated!\n",k);
k++;
}
return 0;
}
