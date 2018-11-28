#include<bits/stdc++.h>
using namespace std;
char s[105],a[105];
int m,l;
void flip_p()
{
    for(int i=0;i<l;i++)
    {
        if(s[i]=='+')
            s[i]='-';
        else
            break;
    }
}
void flip(int k)
{
    int i;
    for(i=0;i<=k;i++)
    {
        if(s[i]=='-')
        {
            a[k-i]='+';
        }
        else
        {
            a[k-i]='-';
        }
    }
    for(i=0;i<=k;i++)
    {
        s[i]=a[i];
    }
}
int main()
{
    int i,t,c;
    scanf("%d",&t);
    for(c=1;c<=t;c++)
    {
        memset(s,'\0',sizeof(s));
        m=0;
        scanf("%s",&s);
        l=strlen(s);
        for(i=l-1;i>=0;i--)
        {
            if(s[i]=='-')
            {
                if(s[0]=='+')
                {
                    flip_p();
                    flip(i);
                    m+=2;
                }
                else
                {
                    flip(i);
                    m+=1;
                }
            }
        }
        printf("Case #%d: %d\n",c,m);
    }
    return 0;
}
