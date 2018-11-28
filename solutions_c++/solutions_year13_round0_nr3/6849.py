#include<iostream>
using namespace std;
int main()
{ int n,a,b,i,j,count;
freopen("input.in","r",stdin);
freopen("output.txt","w",stdout);
scanf("%d\n",&n);
int s[]={1,4,9,121,484};
for(i=0;i<n;i++)
{count=0;
scanf("%d %d\n",&a,&b);
for(j=0;j<5;j++)
if(s[j]>=a && s[j]<=b)
count++;
printf("Case #%d: %d\n",i+1,count);
}
 return 0;
 }
