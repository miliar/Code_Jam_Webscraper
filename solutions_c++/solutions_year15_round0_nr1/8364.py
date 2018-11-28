#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
int t,g;
scanf("%d",&t);

for(g = 1;g<=t;g++)
{
char c[1005];
int n,i,j,x = 0,count = 0;
scanf("%d",&n);
scanf("%s",c);


for(i=0;i<=n;i++)
{
if(i>count) {x = x + (i - count); count = count + (i - count);}
count = count + (c[i] - '0');

}


printf("Case #%d: %d\n",g,x);

}
return 0;
}
