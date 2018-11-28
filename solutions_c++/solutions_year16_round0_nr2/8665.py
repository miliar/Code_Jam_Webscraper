#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main()
{
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int t;
    ll n;
    scanf("%d",&t);
    string str;
    for(int test=1;test<=t;test++)
    {
      printf("Case #%d: ",test);
        cin>>str;
        int nop=0,n=str.size();
        for(int i=n-1;i>=0;i--)
           {
              if(nop%2==0)
                {
                  if(str[i]=='-')nop++;
                }
                else
                {
                 if(str[i]=='+')nop++;
                }
           }
           printf("%d\n",nop);
    }
    return 0;
}
