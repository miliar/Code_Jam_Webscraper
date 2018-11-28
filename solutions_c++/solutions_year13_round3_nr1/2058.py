#include <stdio.h>

char tab[101];
int n,v;

void check(int start, int end)
{
    int i;
    int consonants = 0;

    if(end-start<n)return;

    for(i=start;i<end;i++)
    {
        if(tab[i]!='a' && tab[i]!='e' && tab[i]!='i' && tab[i]!='o' && tab[i]!='u')
        {
            consonants++;
        }
        else
        {
            consonants=0;
        }

        if (consonants >= n)
        {
            v++;
            return;
        }
    }

    return;
}

int main()
{

    int t,j,l,i,end;

    scanf("%d",&t);
    getchar();

    for(j=0;j<t;j++)
    {
        scanf("%s",tab);
        scanf("%d",&n);

        for(l=0;tab[l]!=0;l++);
        v=0;
        end =0;

        for(i=0;i<l;i++)
        {
            for(end=0;end<=l;end++)
            {
                check(i,end);
            }
        }

        printf("Case #%d: %d",j+1,v);
        if(j!=t-1)printf("\n");
    }
    return 0;
}
