#include<cstdio>
#include<algorithm>

using namespace std;

int main()
{
    int i , j , k;
    long long r,t,start;
    int times;
    long long counter;
    scanf("%d",&times);



    for(i = 0 ; i < times; i++)
    {
        scanf("%lld %lld",&r,&t);
        start = ((r+1) * (r+1)) - (r*r);

        long long first =start;
        for(counter = 1; start <= t ; counter++)
        {
            start += first + (4*counter);
        }

        printf("Case #%d: %lld\n",i+1,counter-1);

    }
    return 0;
}
