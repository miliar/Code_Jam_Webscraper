#include <iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("inp.txt","r",stdin);
    freopen("op.txt","w",stdout);
    int pos,te,n,i,ct;
    char s[110],c;
    char lom[110];
    int k=0,fl;
    scanf("%d",&te);
    while(--te>=0)
    {
        k++;
        ct=0;
        fl=1;
        while((c=getchar())!='\n')
            ;
        scanf("%s",s);
        n=strlen(s);
        for(i=n-1;i>=0;i--)
        {
            if(s[i]=='+')
                continue;
            else
                break;
        }
        pos=i;
        if(i<0)
            ;
        else
        {
            while(fl==1)
            {
                if(s[0]=='+')
                    ct++;
                for(i=0;i<pos;i++)
                {
                    if(s[i]=='+')
                        s[i]='-';
                    else
                        break;
                }
                for(i=0;i<=pos;i++)
                {
                    if(s[i]=='+')
                        s[i]='-';
                    else if(s[i]=='-')
                        s[i]='+';
                    lom[i]=s[i];
                }
                for(i=0;i<=pos;i++)
                {
                    s[i]=lom[pos-i];
                }
                ct++;
                for(i=pos-1;i>=0;i--)
                {
                    if(s[i]=='+')
                        continue;
                    else
                        break;
                }
                if(i<0)
                    fl=0;
                else
                    pos=i;
            }
        }
        printf("Case #%d: %d\n",k,ct);
    }
    return 0;
}
