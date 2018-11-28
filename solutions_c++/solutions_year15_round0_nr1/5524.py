#include <bits/stdc++.h>
using namespace std;
char s[1005],c;
int n,t,a,b;
int main ()
{
//freopen("A-large.in","r",stdin);
//freopen("Output.txt","w",stdout);
cin>>t;

for(int j=1;j<=t;j++)
    {
       scanf("%d%s",&n,s);
       a=b=0;
       for(int i=0;i<=n;i++)
       {
         if(s[i]!='0' && a<i){b+=(i-a);a=i;}
         a+=(int(s[i])-48);
       }
       printf("Case #%d: %d\n",j,b);
    }
return 0;
}
