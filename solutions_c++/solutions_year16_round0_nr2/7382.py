#include<bits/stdc++.h>
using namespace std;
int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
    char ar[150];
    int t,cs,i,ln,cou;
    scanf("%d",&t);
    gets(ar);
    for(cs=1;cs<=t;cs++)
    {
        gets(ar);
        cou=0;
        ln=strlen(ar)-1;
        while(ln!=-1)
        {
            if(ar[ln]=='+'){
                ln--;
                continue;
            }
            else{
                cou++;
                if(ar[0]=='+')
                {
                    cou++;
                    i=0;
                    while(ar[i]!='-')
                    {
                        ar[i]='-';
                        i++;
                    }
                }
                stack<char> ch;
                while(!ch.empty()) {ch.pop();}

                for(i=0;i<=ln;i++)
                {
                    ch.push(ar[i]);
                }
                i=0;
                while(!ch.empty())
                {
                    char nw=ch.top();
                    ch.pop();
                    if(nw=='-')
                        ar[i++]='+';
                    else ar[i++]='-';

                }
                ln--;
            }
        }
        printf("Case #%d: %d\n",cs,cou);
    }

    return 0;
}
