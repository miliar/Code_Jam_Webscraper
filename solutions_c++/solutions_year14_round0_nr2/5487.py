#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int kasus;
double jawab,c,f,x,tampung,spd;

inline bool masih()
{
    //antara kalau beli dan langsung
    return (c + x*spd/(spd+f)) <= x;
}

int main()
{
//    freopen("B-large.in","r",stdin);
//    freopen("b.out","w",stdout);
    
    scanf("%d",&kasus);
    for (int z=1;z<=kasus;z++)
    {
        scanf("%lf %lf %lf",&c,&f,&x);
        jawab = tampung = 0.00;
        spd = 2.00;
        while (masih())
        {
            tampung = 0.00;
            jawab += c/spd;
            spd += f;
        }
        jawab += (max(x,x-c))/spd;
        printf("Case #%d: %.7lf\n",z,jawab);
    }
    return 0;
}
