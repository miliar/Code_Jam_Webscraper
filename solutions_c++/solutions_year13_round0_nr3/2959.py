#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>

using namespace std;

bool is_palin(long long num)
{
    int x=0;
    long long temp = num;
    while((temp/=10))
        x++;

    long long num2=0;
    long long num1 = num;
    for(int i=x; i>=0; i--)
    {
        temp=num%10;
        num/=10;
        num2+=temp*pow(10,i);
    }

    if(num1==num2)
        return true;
    else
        return false;
}


int main()
{
    //freopen("C-small-attempt0.in", "r", stdin);
    //freopen("result.txt", "w", stdout);
    int T;
    scanf("%d", &T);

    for(int t=1; t<=T; t++)
    {
        long long A, B;

        scanf("%lld %lld", &A, &B);

        int count=0;
        long long sqr;
        for(long long i = A; i<=B; i++)
        {
            if(is_palin(i))
            {
                sqr = sqrt(i);

                if( sqr*sqr == i && is_palin(sqr))
                    count++;
            }
        }

        cout<<"Case #"<<t<<": "<<count<<endl;
    }
    return 0;
}
