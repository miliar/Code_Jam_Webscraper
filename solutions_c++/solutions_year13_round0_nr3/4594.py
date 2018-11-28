#include<iostream>
#include<iomanip>
#include<math.h>
#include<stdlib.h>
#include<stdio.h>
#include<algorithm>
using namespace std;
int isPalindrome(long j)
{
long rev=0;
long rem=j;
while(rem!=0){
rev=rev*10+rem%10;
rem=rem/10;
}
if(rev==j)
return 1;
else return 0;
}

int main()
{
int T;
double a,b,count=0,temp,ans[101];
long sqa,sqb;
cin>>T;
for(int i=0;i<T;i++)
{
count=0;
cin>>a;
cin.ignore(256,' ');
cin>>b;
cin.ignore(256,'\n');
sqa=(long)ceil(sqrt(a));
sqb=(long)floor(sqrt(b));
for(long j=sqa;j<=sqb;j++)
{
if(isPalindrome(j))
if(isPalindrome(j*j))
count++;
}
ans[i]=count;
}
for(int i=0;i<T;i++)
printf("Case #%d: %.0f\n",(i+1),ans[i]);
return 0;
}
