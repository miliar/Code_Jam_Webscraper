#include<bits/stdc++.h>
using namespace std;
int check(int *a)
{
    int i;
    for(i=0;i<10;i++)
        if(a[i]==0)
            return 1;
    return 0;    
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,z=1;
    scanf("%d",&t);

    while(z<=t)
    {
        char s[110];
        scanf("%s",s);
        int len=strlen(s);
        int i=len-1;
        int count=0;
        while(s[i]=='+')
        {
           i--;
           if(i<0)
                break;
        }
        if(i>=0&&s[i]=='-')
        {
            count++;
            i--;
        }
        for(;i>=0;i--)
        {
                if(s[i]=='-'&&s[i+1]=='+')
                {
                    count++;
                    continue;
                }
                if(s[i]=='+'&&s[i+1]=='-')
                    count++;
        }
        printf("Case #%d: %d\n",z,count);
        z++;
    }
    return 0;
}