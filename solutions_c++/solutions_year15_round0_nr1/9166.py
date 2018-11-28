#include<cstdio>
#include<cstring>
#include<cmath>
#include<string>
#include<iostream>
using namespace std;


int test,num,tst=1;
char line[1007];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

   scanf("%d",&test);
   while(test--)
   {
       string s="";
       scanf("%d",&num);
       scanf(" %s", line);
      int  cnt=0,ans=0;
        int k=1,p=line[0]-'0';
       for(int i=1;i<num+1;i++)
       {

          if(p<k)
          {
              ans+=(k-p);
              p+=(k-p);
          }
          p+=(line[i]-'0');
          k++;
       }

       printf("Case #%d: %d\n",tst++,ans);
   }
   return 0;
}
