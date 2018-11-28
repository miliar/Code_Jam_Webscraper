#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

int main()
{

long long int t,s,i,sum,answer,len,j;

char str[1001];

scanf("%lld",&t);
j=1;
while(t--)
{
memset(str,'\0',1001);
sum=0;
answer=0;
scanf("%lld",&s);
scanf("%s",str);
i=0;
len=strlen(str);
while(i<len)
{
if(sum<i)
{
answer=answer+i-sum;
sum=sum+i-sum+(int)str[i]-'0';
}
else
sum=sum+(int)str[i]-'0';
i++;
}

printf("Case #%lld: %lld\n",j,answer);
j++;

}
return 0;
}

