#include<stdio.h>
#include<string.h>
#include<math.h>
#include<string>
#include<vector>
#include<map>
#include<algorithm>
#include<iostream>
#include<queue>
#include<set>
using namespace std;
#define PI 2 * acos (0.0)

bool P[1010];

bool pelindrom(int x)
{
    int i,j,k,a[10];
    i=0;
    while(x)
    {
        a[i++]=x%10;
        x/=10;

    }
    for(j=0,k=i-1;j<=k;j++,k--)
        if(a[j]!=a[k])
        return false;
    return true;
}
void precal()
{
    int i;
    memset(P,false,sizeof(P));
    for(i=1;i<=100;i++)
    {
        if(pelindrom(i) && pelindrom(i*i))
            P[i*i]=true;

    }
    /*
    for(i=0;i<1001;i++)
        if(P[i])
        cout<<i<<","<<sqrt(i)<<" ";
        //*/
}
int main()
{
    precal();
    freopen("C:\\Users\\talha\\Desktop\\Google_CJ_2013\\C-small-attempt0.in","r",stdin);
    freopen("C:\\Users\\talha\\Desktop\\Google_CJ_2013\\C-small-attempt0.out","w",stdout);
    int a,b,i,c,tc,t=1;
    scanf("%d",&tc);
    while(tc--)
    {
        scanf("%d %d",&a,&b);
        c=0;
        for(i=a;i<=b;i++)
            if(P[i])
            c++;
        printf("Case #%d: %d\n",t++,c);

    }
    return 0;
}
