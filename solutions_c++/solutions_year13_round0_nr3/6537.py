#include<cstdio>
#include<iostream>
#include <algorithm>
#include<cmath>

using namespace std;

bool isPalin(unsigned long long x)
{
    unsigned long long y=x,z=0,z1,z2;
    while(y>0)
    {
        z1=y%10;
        y/=10;
        z=z*10+z1;
    }
    if(x==z)
        return true;
    return false;
}

int main()
{
    int t;
    scanf("%d\n",&t);
    for(int z=0;z<t;z++)
    {
        unsigned long long A,B,ans=0;
        scanf("%llu %llu",&A,&B);
        int start=sqrt(A);
        for(int i=start;i*i<=B;i++)
        {
            if(isPalin(i*i)&&i*i>=A&&i*i<=B&&isPalin(i)){
                ans++;
            }
        }
        //printf("%llu %llu",A,B);
        cout<<"Case #"<<(z+1)<<": "<<ans<<endl;


    }
    return 0;
}


