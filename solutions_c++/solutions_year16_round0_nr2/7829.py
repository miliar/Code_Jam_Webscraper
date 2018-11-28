#include<bits/stdc++.h>


using namespace std;

int main()
{
    //freopen("B-large (3).in","r",stdin);
    //freopen("btestlarge3.out","w",stdout);

    int i,t,c,f,j;
    char s[150];
    scanf("%d",&t);
    for(i=1;i<=t;++i)
    {
        c=j=0;
        scanf("%s",s);
        while(s[j]!='\0' && s[j]=='-')
            j++;
        if(j!=0)
            c++;
        f=0;
        for(;s[j]!='\0';++j)
        {
            if(s[j]=='-')
                f++;
            if(s[j]=='+')
            {
                if(f!=0)
                    c+=2;
                f=0;
            }
        }
        if(f!=0)
            c+=2;
        printf("Case #%d: %d\n",i,c);

    }


    return 0;
}
