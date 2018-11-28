#include<bits/stdc++.h>
using namespace std;
int ar[10];
void f(int &z , long long n)
{
    while(n)
    {
        if(!ar[n % 10])
            z ++;
        ar[n % 10] = 1 ,  n /= 10;
    }
}
int main()
{
    long long n , m;
    int t , z;
    freopen("Counting Sheep.in" , "r" , stdin);
    freopen("Counting Sheep.out" , "w" , stdout);
    scanf("%d",&t);
    for(int i = 1 ; i <= t ;i ++){
        scanf("%lld",&n);
        z = 0 , m = n;
        memset(ar , 0 , sizeof ar);
        f(z , n);
        int cnt = 0;
        for(; z < 10 && cnt < 10000010; cnt ++)
            n += m , f(z , n ) ;
        printf("Case #%d: " , i);
        if(z < 10)
            printf("INSOMNIA\n");
        else printf("%lld\n",n);
    }
}
