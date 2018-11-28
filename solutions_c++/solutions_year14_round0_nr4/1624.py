#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
using namespace std ;


int main()
{
    freopen("D-large.in","r",stdin);
    freopen("output.large","w",stdout);

    int cases;
    scanf("%d",&cases);
    int a[1005];
    int b[1005];

    for(int c = 1; c <= cases ; c++)
    {
        int totalround;
        scanf("%d",&totalround);
        
        for(int z = 0 ; z < totalround ; z++)
        {
            double tmp;
            scanf("%lf",&tmp);
            a[z] = (int)(tmp*100000);
        }
        for(int z = 0 ; z < totalround ; z++)
        {
            double tmp;
            scanf("%lf",&tmp);
            b[z] = (int)(tmp*100000);
        }
        
        sort(a,a+totalround);
        sort(b,b+totalround);
        
        int ans1=0 ;
        int ans2=totalround ;
        int naomiflag = 0;
        for(int i = 0 ; i < totalround ; i++)   //ken
        {
            if(b[i]>a[naomiflag])
            {
                ans2--;
                naomiflag++;
            }
        }
        
        int kenflag = 0;
        for(int i = 0 ; i < totalround ; i++)   //naomi
        {
            if(a[i]>b[kenflag])
            {
                ans1++;
                kenflag++;
            }
        }
        
        printf("Case #%d: %d %d\n",c,ans1,ans2);
    }
    return 0;
}