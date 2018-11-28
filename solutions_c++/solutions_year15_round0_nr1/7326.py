#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("123.txt","w",stdout);
    char data[2000];
    int level;
    int t;
    int cur;
    int ans;
    int cot=0;
    scanf("%d",&t);
    while(t--)
    {

        scanf("%d",&level);
        scanf("%s",data);
        cur=0;
        ans=0;
        for(int i=0;i<=level;i++)
        {
            if(data[i]>'0')
            {
                if(cur>=i)cur+=data[i]-'0';
                else
                {
                    ans+=i-cur;
                    cur=i+data[i]-'0';
                }
            }
        }
        printf("Case #%d: ",++cot);
        printf("%d\n",ans);
    }
    return 0;
}
