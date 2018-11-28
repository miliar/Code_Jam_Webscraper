#include<stdio.h>
#include<string.h>

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("Blarge.txt","w",stdout);
    int i,t,len,co=1;
    char s[109],ch;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%s",s);
        ch=s[0];
        len=1;
        for(i=1;s[i]!=0;i++)
        {
            if(s[i]!=ch)
            {
                ch=s[i];
                len++;
            }
        }
        if(len%2==0)
        {
            if(s[0]=='+')
                printf("Case #%d: %d\n",co++,len);
            else
                printf("Case #%d: %d\n",co++,len-1);
        }
        else
        {
            if(s[0]=='+')
                printf("Case #%d: %d\n",co++,len-1);
            else
                printf("Case #%d: %d\n",co++,len);
        }
    }
    return 0;
}
