#include<iostream>
#include<cstdio>
#include<string.h>

using namespace std;

int main()
{
    freopen("input.in", "r", stdin);
    freopen ("output.txt","w",stdout);
    int Test,k=0;
    scanf("%d",&Test);
    while(Test--)
    {
        k++;
        char S[101];
        scanf("%s",&S);
        printf("Case #%d: ",k);
        int i,len=strlen(S),flag=0,ans=0,pre=0,t=0;
        for(i=0;i<len;i++)
        {
            if(flag)
            {
                if(S[i]=='+')
                {
                    if(pre==1 || t==1)
                    {
                        ans+=2;
                        pre=0;
                    }
                    else
                    {
                        ans++;
                    }
                    t=1;
                    flag=0;
                }
            }
            else
            {
                if(S[i]=='+')
                {
                    t=1;
                    pre=1;
                }
                else
                {
                    flag=1;
                }
            }
            //cout<<i<<" "<<ans<<endl;
        }
        if(flag)
        {
            if(pre==1 || t==1)
            {
                ans+=2;
                pre=0;
            }
            else
                ans++;
        }
        printf("%d\n",ans);
    }
    fclose(stdout);
    return 0;
}
