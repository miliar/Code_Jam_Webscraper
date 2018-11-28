#include <iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
char s[102];
int main()
{
    freopen("input2.in","r",stdin);
    freopen("output2.txt","w",stdout);
    int t,ans,j,c=1;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%s",&s);
        ans=0;
        int l=strlen(s);
        int i=0;
        for(;;)
        {
            if(s[i]=='+')
            {
                for( j=i; j<l&&s[j]=='+'; j++);
                if(j==l) break;
                else
                {
                    for(int k=j-1; k>=0; k--)
                        s[k]='-';
                }
                ans++;
            }
            else
            {
                for( j=i; j<l&&s[j]=='-'; j++);
                if(j==l)
                {
                    ans++;
                    break;
                }
                else
                {
                    for(int k=j-1; k>=0; k--)
                        s[k]='+';
                }
                ans++;
            }

        }
        printf("Case #%d: %d\n",c,ans);
        c++;
    }
    return 0;
}
