#include<stdio.h>
#include<string.h>

char st[110],s[110];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,ti,i,j,k,l;
    scanf("%d",&t);
    for(ti=1; ti<=t; ++ti)
    {
        scanf("%s",&st);
        l=strlen(st);
        s[0]=st[0];
        j=0;
        for(i=1; i<l; ++i)
        {
            if(st[i] != s[j])
            {
                s[++j]=st[i];
            }
        }
        s[++j]='\0';
        l=strlen(s);
        if(s[l-1]=='+')
            --l;
        printf("Case #%d: %d\n",ti,l);
    }
    return 0;
}
