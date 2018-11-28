#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;
class cmp
{
public:

    int operator()(const float A,const float B)
    {
        return A<B;
    }
};
int t;
int n;
float naomi[1005],ken[1005];
int viz[1005];
void re()
{
    for(int i=1;i<=n;i++)
        viz[i]=0;
}
void citire()
{
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
        scanf("%f",&naomi[i]);
    for(int i=1;i<=n;i++)
        scanf("%f",&ken[i]);
    sort(naomi+1,naomi+n+1,cmp());
    sort(ken+1,ken+n+1,cmp());
}
void afisare()
{
    for(int i=1;i<=n;i++)
        printf("%f ",naomi[i]);
    printf("\n");
    for(int i=1;i<=n;i++)
        printf("%f ",ken[i]);
            printf("\n");
}
void rez()
{
    for(int i=1;i<=n;i++)
        for(int j=1;j<=n;j++)
            if(naomi[i]>ken[j] && !viz[j])
                {viz[j]=1;break;}
    int k=0;
        for(int i=1;i<=n;i++)
            k+=viz[i];
    printf("%d ",k);
    re();
    for(int i=1;i<=n;i++)
        for(int j=1;j<=n;j++)
            if(ken[j]>naomi[i] && !viz[j])
                {viz[j]=1;break;}
    k=n;
    for(int i=1;i<=n;i++)
        k-=viz[i];
    printf("%d",k);
}
int main()
{
    freopen("jam.in","r",stdin);
    freopen("jam.out","w",stdout);
    scanf("%d",&t);
    for(int run=1;run<=t;run++)
    {
        citire();
        printf("Case #%d: ",run);
        rez();
        printf("\n");
        re();
    }

    return 0;
}
