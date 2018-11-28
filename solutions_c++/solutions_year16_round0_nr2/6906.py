#include <cstdio>
#include <cstring>

using namespace std;

int verif(char s[])
{
    int l=strlen(s)-1;
    for(int i=0;i<=l;i++)
        if(s[i]=='-')
            return 0;
    return 1;
}

int main()
{
    freopen("pancake.in","r",stdin);
    freopen("pancake.out","w",stdout);
    int n, nr;
    char s[101];
    scanf("%d\n",&n);
    for(int i=1;i<=n;i++)
    {
        scanf("%s\n", s);
        nr=0;
        int j=0, l=strlen(s), ok=0;
        if(verif(s)==1)
            {printf("CASE #%d: %d\n", i, nr);ok=1;}
        else
            nr++;
        do{
        while(j<=l && s[j]!='+' && ok==0)
             {
                 s[j]='+';
                 j++;
             }
        if(verif(s)==1 && ok==0)
            {printf("CASE #%d: %d\n", i, nr);ok=1;}
        else
            if(j>0)
            nr++;
        while(j<=l && s[j]=='+' && ok==0)
              j++;
        if(j<l && ok==0)
         {for(int k=0;k<j;k++)
               s[j]='-';
               nr+=1;
         }
        }while(j<=l && ok==0);
    }
    return 0;
}
