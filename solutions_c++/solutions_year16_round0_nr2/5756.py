#include<stdio.h>
#include<string.h>
#include<iostream>

using namespace std;

int main()
{
    char s[1000];
    int length,i,j,flip=0,plus=0,minus=0,ps=0,pe=0,ms=0,me=0,pe2=0,t,cases,flag=1;

    freopen("problem2large.in","r",stdin);
    freopen("problem2large.out","w",stdout);
    scanf("%d",&t);
    for(cases=1;cases<=t;cases++)
    {

    std::cin>>s;
    length=strlen(s);

    for(i=0;i<=length-1;i++)
    {
        if(s[i]=='+')
        {
            plus++;
        }
        else if(s[i]=='-')
        {
            minus++;
        }
    }
    if(plus==length)
    {
        flip=0;
        flag=0;
    }
    else if(minus==length)
    {
        flip=1;
        flag=0;
    }


    while(flag==1)
    {
    if(s[0]=='+' && s[length-1]=='+')
    {
        for(i=0;i<=length-1;i++)
        {
            if(s[i]=='+')
            {
                ps++;
            }
            else
            {
                break;
            }
        }
        for(i=length-1;i>=0;i--)
        {
            if(s[i]=='+')
            {
                pe++;
            }
            else
            {
                break;
            }
        }
        for(i=0;i<=length-1-pe;i++)
        {
            if(s[i]=='+')
            {
                s[i]='-';
            }
            else if(s[i]=='-')
            {
                s[i]='+';
            }
        }
        flip++;
        ps=0;
        pe=0;
    }

    else if(s[0]=='-' && s[length-1]=='-')
    {
        for(i=0;i<=length-1;i++)
        {
            if(s[i]=='-')
            {
                ms++;
            }
            else
            {
                break;
            }
        }
        for(i=length-1;i>=0;i--)
        {
            if(s[i]=='-')
            {
                me++;
            }
            else
            {
                break;
            }
        }
        for(i=0;i<=length-1;i++)
        {
            if(s[i]=='+')
            {
                s[i]='-';
            }
            else if(s[i]=='-')
            {
                s[i]='+';
            }
        }
        flip++;
        ms=0;
        me=0;
    }

    else if(s[0]=='-' && s[length-1]=='+')
    {
        for(i=length-1;i>=0;i--)
        {
            if(s[i]=='+')
            {
                pe2++;
            }
            else
            {
                break;
            }
        }
        for(i=0;i<=length-1-pe2;i++)
        {
            if(s[i]=='+')
            {
                s[i]='-';
            }
            else if(s[i]=='-')
            {
                s[i]='+';
            }
        }
        flip++;
        pe2=0;
    }

    else if(s[0]=='+' && s[length-1]=='-')
    {
        for(i=0;i<=length-1;i++)
        {
            if(s[i]=='+')
            {
                s[i]='-';
            }
            else if(s[i]=='-')
            {
                s[i]='+';
            }
        }
        flip++;
    }

    for(i=0;i<=length-1;i++)
    {
        if(s[i]=='+')
        {
            flag=0;
        }
        else
        {
            flag=1;
            break;
        }
    }
    }

    printf("Case #%d: %d\n",cases,flip);
    flip=0;
    plus=0;
    minus=0;
    ps=0;
    pe=0;
    ms=0;
    me=0;
    pe2=0;
    flag=1;
    }
    return 0;
}
