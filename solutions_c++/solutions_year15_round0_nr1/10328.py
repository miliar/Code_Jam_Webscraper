#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;

int main()
{
int j,t,smax,i,length,pplstanding,pplreqd;
char s[10];
scanf("%d",&t);
for(j=1;j<=t;j++)
{

scanf("%d",&smax);
scanf("%s",s);
length=strlen(s);
pplstanding=s[0]-'0';
pplreqd=0;
for(i=1;i<length;i++)
{
if((s[i]-'0')!=0)
{
    if(pplstanding<i)
    {


pplreqd=pplreqd+i-pplstanding;
pplstanding=s[i]-'0'+i;
}
else
pplstanding=pplstanding+s[i]-'0';
}
}
printf("Case #%d: %d\n",j,pplreqd);
}
return 0;

}
