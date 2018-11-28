#include<stdio.h>
int main(void)
{
    //freopen("ou.txt","w",stdout);
    //freopen("in.txt","r",stdin);
    int t,c=0;
    scanf("%d",&t);
    while(t--)
    {
        printf("Case #%d: ",++c);
        char s[1005];
        int num;
        scanf("%d",&num);
        scanf("%s",s);
        int len=num+1;
        int ans=0;
        int temp=s[0]-'0',i;
        for(i=1;i<num;++i)
        {
            if(s[i]=='0')
                continue;
            if(temp>=num)
                break;
            if(temp>=i)
            {
                temp+=s[i]-'0';
            }
            else
            {
                ans+=i-temp;
                temp+=i-temp;
                temp+=s[i]-'0';
            }
        }
        if(temp<num)
        {
            printf("%d\n",ans+num-temp);
        }
        else
        {
            printf("%d\n",ans);
        }
    }
    return 0;
}
