#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
int sq[2002];
bool istrue(int t)
{
    if(t==1000||t==0)
        return false;

    int n=t;
    int a=n%10;
    n=n/10;
    if(n==0)
        return true ;
    int b=n%10;
    n=n/10;
    if(n==0)
        return a==b;
    int c=n%10;
    return a==c;

}
int main()
{
    freopen("C-small.in","r",stdin);
    freopen("c-small.out","w",stdout);
    int cas;
    scanf("%d",&cas);
    for(int i=0; i<=1000; i++)
        sq[i]=0;
    for(int i=1; i*i<=1000; i++)
    {
        sq[i*i]=i;

    }
    for(int C=1; C<=cas; C++)
    {
        printf("Case #%d: ",C);
        int a,b;
        scanf("%d %d",&a,&b);
        int ans=0;
        for(int i=a; i<=b; i++)
        {
            if(istrue(i)&&istrue(sq[i]))
                {
                    ans++;
                    //printf("%d\n",i);
                }
        }
        printf("%d\n",ans);
    }
    return 0;
}
