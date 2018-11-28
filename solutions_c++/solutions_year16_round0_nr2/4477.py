#include<stdio.h>
#include<string.h>
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,i,j,k;
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
        char s[101];
        int l,c=0;
        scanf("%s",s);
        l=strlen(s);
        for(j=0;j<l-1;j++)
        {
            if(s[j]==s[j+1])
                continue;
                else
                    c++;

        }
        if(s[l-1]=='+')
            printf("case #%d: %d\n",i+1,c);
        else
             printf("case #%d: %d\n",i+1,c+1);


    }
    return 0;
}

