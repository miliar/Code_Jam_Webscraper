#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,x=0;
    scanf("%d",&t);
    while(t--)
    {
        char str[205];
        ++x;
        int ans=0;
        scanf(" %s",str);
        for(int i=0;str[i]!=0;)
        {
            if(i==0&&str[i]=='-')
              {
                  ans++;

              }
            else if(str[i]=='-')
             ans=ans+2;
            while(str[i]!=0&&str[i]=='-')
              i++;
              if(str[i]=='+')
              i++;
        }

        printf("Case #%d: ",x);
        printf("%d\n",ans);
   }
    return 0;
}

