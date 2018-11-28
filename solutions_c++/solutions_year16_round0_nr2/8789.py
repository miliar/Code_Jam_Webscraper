#include<cstdio>

int main()
{
    int tt;
    scanf("%d",&tt);
    for(int t=1;t<=tt;t++)
    {
        char s[200];
        scanf("%s",s);
        char cur = s[0];
        int count = 0;
        for(int i=0;s[i]!='\0';i++)
        {
            if(cur != s[i])
            {
                cur = s[i];
                count++;
            }
        }
        if(cur == '-') count++;
        printf("Case #%d: %d\n",t,count);
    }
    return 0;
}
