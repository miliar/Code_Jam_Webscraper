#include <cstdio>
int main()
{
    int T,l=1,N,NKopia,ilo,j;
    bool tab[10];
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&N);
        if(N==0)
        {
            printf("Case #%d: INSOMNIA\n",l);
            l++;
            continue;
        }

        j=1;
        ilo=10;
        for(int i=0; i<10; i++)
            tab[i]=false;


        while(666)
        {
            NKopia=N*j;
            while(NKopia>0)
            {
                if(!tab[NKopia%10])
                {
                    tab[NKopia%10]=true;
                    ilo--;
                }
                NKopia/=10;
            }
            NKopia=N*j;
            if(ilo==0) break;
            j++;

        }


        printf("Case #%d: ",l);
        printf("%d\n",NKopia);
        l++;
    }

    return 0;
}
