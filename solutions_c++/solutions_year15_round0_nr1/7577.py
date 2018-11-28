/* Ashish Jain
E-mail-ashish.jain@outlook.in*/
#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int main()
{
long long int t,i,j,n,sm,c,l,p;
scanf("%lld",&t);
for(j=1;j<=t;j++)
{
c=0;
l=0;
p=0;
char s[1005];
scanf("%lld",&sm);
//scanf("%s",s);
cin>>s;
n=sm+1;
l=(long long int)(s[0]-'0');
for(i=1;i<n;i++)
{
if(l<i && s[i]!='0')
{
 c=i-l;
 p+=c;
 l+=c;
}
l=l+(long long int)(s[i]-'0');
}
printf("Case #%lld: %lld\n",j,p);
}

return 0;
}
