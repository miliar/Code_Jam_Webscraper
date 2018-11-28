#include<cstdio>
#include<algorithm>

using namespace std;

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for ( int te=1 ; te<=t ; te++ )
    {
        int K,C,S;
        scanf("%d%d%d",&K,&C,&S);
        printf("Case #%d: ",te);
        for ( int c=1 ; c<=K ; c++ )
            printf("%d ",c);
        printf("\n");
    }
}
