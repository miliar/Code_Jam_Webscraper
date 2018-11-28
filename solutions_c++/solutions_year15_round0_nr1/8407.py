#include <cstdio>

int main()
{
    int t,m,cnt=0,n=0;
    char s[1500];
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        cnt=0;
        n=0;
        scanf("%d",&m);
        scanf("%s",s);
        if(s[0]=='0')
        {
            s[0]='1';
            n++;
            cnt++;
        }
        else n+=s[0]-'0';
        for(int j=1;j<=m;j++)
        {
            if(s[j]!='0')
            {
                if(j<=n) n+=s[j]-'0';
                else
                {
                    cnt+=j-n;
                    n+=j-n+s[j]-'0';
                }
            }
        }
        printf("Case #%d: %d\n",i+1,cnt);
    }

    return 0;
}
