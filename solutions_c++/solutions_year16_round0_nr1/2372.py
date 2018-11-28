#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input1.in","r+",stdin);
    freopen("output1.txt","w+",stdout);
    int T;
    scanf("%d",&T);
    for(int e = 0 ; e<T;++e)
    {
        printf("Case #%d: ",e+1);
        int N , save  , mask = 0 , i ;
        scanf("%d",&N);
        if(N==0)
        {
            printf("INSOMNIA\n");
            continue;
        }

        for(i=1 , save = N;__builtin_popcount(mask)!=10;save = N * i )
        {
            while(save)
            {
                mask|=1<<(save%10);
                save/=10;
            }
            ++i;
        }
        printf("%d\n",(i-1)*N);
    }

    return 0;
}
