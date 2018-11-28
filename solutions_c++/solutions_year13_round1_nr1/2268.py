#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int n,t,r,d,tmp,i,j;
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        scanf("%d%d",&r,&t);
        d=r+1;
        tmp=d*d-r*r;
        j=0;
        while(tmp<=t)
        {
            t=t-tmp;
            r=r+2;
            d=d+2;
            j++;
            tmp=d*d-r*r;
        }
        printf("Case #%d: %d\n",i,j);
    }
    return 0;
}
