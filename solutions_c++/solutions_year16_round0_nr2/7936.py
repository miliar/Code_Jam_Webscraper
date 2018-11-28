#include<bits/stdc++.h>

using namespace std;

char str[110];

void func(int len,char ch)
{
    int i,j;
    char t;

    if(ch=='+')
        t='-';
    else if(ch=='-')
        t='+';

    for(i=0;i<len;i++)
        str[i]=t;

}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int t;
    int i,j,k;
    k=0;
    scanf("%d",&t);

    while(t--)
    {
        k++;
        scanf("%s",str);
        int c=0;
        int len=strlen(str);
        char ch;
        int g=len+1;

        while(g--)
        {
            ch=str[0];

            for(i=0;i<len;i++)
                if(str[i]!=ch)
                    break;

            if(i==len && ch=='+')
                break;
            else if(i==len && ch=='-')
            {
                c++;
                break;
            }

            func(i,ch);
            c++;
        }

        printf("Case #%d: %d\n",k,c);
    }

    return 0;
}
