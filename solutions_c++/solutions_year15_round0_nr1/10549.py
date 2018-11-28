#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main()
{
    int test;
    cin>>test;
    for(int co1=1;co1<=test;co1++){
        int smax,ans=0;
        cin>>smax;
        int a[smax+1];
        int stand=0;
        scanf("%d",&stand);
        for(int co2=smax;co2>=0;co2--){
            a[co2]=stand%10;
            stand/=10;
        }
        for(int co2=1;co2<smax+1;co2++){
            int temp=0;
            if(a[co2]>0){
                for(int co3=0;co3<co2;co3++){
                    temp+=a[co3];
                }
                if(temp<co2){
                    ans+=(co2-temp);
                    a[0]+=(co2-temp);
                }
            }
        }
        printf("Case #%d: %d\n",co1,ans);
    }
    return 0;
}
