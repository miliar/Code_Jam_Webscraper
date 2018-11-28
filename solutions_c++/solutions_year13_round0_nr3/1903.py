#include<stdio.h>

typedef long long ll;

ll save[] = {1LL, 4LL, 9LL, 121LL, 484LL, 10201LL, 12321LL, 14641LL, 40804LL, 44944LL,
             1002001LL, 1234321LL, 4008004LL, 100020001LL, 102030201LL, 104060401, 121242121LL, 123454321LL, 125686521LL, 400080004LL,
             404090404LL, 10000200001LL, 10221412201LL, 12102420121LL, 12345654321LL, 40000800004LL, 1000002000001LL, 1002003002001LL, 1004006004001LL, 1020304030201LL,
             1022325232201LL, 1024348434201LL, 1210024200121LL, 1212225222121LL, 1214428244121LL, 1232346432321LL, 1234567654321LL, 4000008000004LL, 4004009004004LL };


int main()
{
    freopen("C.in","r",stdin);
    freopen("Cout.out","w",stdout);
    int T, kas=1, i, j;
    ll A, B;

    for(scanf("%d",&T); kas<=T; kas++)
    {
        scanf("%lld%lld",&A,&B);
        for(i=0; i<40; i++)if(save[i]>B) break;
        for(j=0; j<40; j++)if( save[j]>(A-1) )break;

        if(i>39)i=39;
        if(j>39)j=39;

        printf("Case #%d: %d\n",kas,i-j);
    }

    return 0;
}
