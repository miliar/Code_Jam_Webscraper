#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;
char ch[2005];
int main()
{
//    freopen("A-large.in","r",stdin);
//    freopen("out.out","w",stdout);
    int t;
    int cnt=1;
    scanf("%d",&t);
    while(t--)
    {
        int smax;
        scanf("%d",&smax);
        scanf("%s",ch);
        int ans=0;
        int pos2=0;
        for(int i=0; i<=smax; i++)
        {
            if(ch[i]=='0')
                continue;
            else
            {
                if(i<=pos2)
                {
                    pos2+=ch[i]-'0';
                }
                else
                {
                    ans+=i-pos2;
                    pos2+=i-pos2;
                    pos2+=ch[i]-'0';
                }
            }
        }
        printf("Case #%d: %d\n",cnt++,ans);
    }
    return 0;
}
