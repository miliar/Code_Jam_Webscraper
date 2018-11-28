#include<cstdio>
using namespace std;
int main()
{
    int t,i,j;
    int k,c,s;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d%d%d",&k,&c,&s);
        printf("Case #%d:",i);
        for(j=1;j<=s;j++)
            printf(" %d",j);
        printf("\n");
    }
}
