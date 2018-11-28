#include<iostream>
#include<cstring>
#include<cstdio>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<string.h>
#include<cstdlib>
#include<cmath>
using namespace std;
char s[100];
bool  ispal(int n)
{
char *s2;
    int i=0;
    while(n )
    {
          s[i++] = n%10 +'0';
          n=n/10;
    }
    s[i]='\0';
   int l=strlen(s);
     for(int i=0;i<l/2;i++)
     {
         if(s[i] != s[l-1-i])
         return false;
     }

    return true;
}


int main()
{
int   count,n1,n2,i,j,l,t,w;
cin>>t;
w=1;
while(t--){
cin>>n1>>n2;
   l=(int)sqrt(n1);
   if(l*l != n1)
   {
        l++;
   }
   count=0;
   for(i=l ,n1=l*l;  ;i = i++)
   {
       n1 = i*i;
       if(n1>n2)
       break;
       if(ispal(i))
       {
      if(ispal(n1))
     {  //cout<<"palindrome"<<"   "<<n1<<endl;
        count++;
     }}
   }
    printf("Case #%d: %d\n",w++,count);
  }
return 0;
}
