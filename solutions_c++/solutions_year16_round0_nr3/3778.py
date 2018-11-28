#include<iostream>
#include<stdio.h>
#include<cmath>
#include <bitset>
using namespace std ;

long long power(int base,int exp)
{
    if (exp==1)
        return base;
    if (exp==0)
        return 1;
    if ( exp!=1 )
        return (base*power(base,exp-1));
}
long long chk_prime (long long num)
{
    if (num == 2)
        return (-1);
    else if (num % 2 == 0)
        return (2);
    else
    {
        long long divisor = 3;
        double num_d = static_cast<double>(num);
        long long upperLimit = static_cast<long long>(sqrt(num_d) +1);

        while (divisor <= upperLimit)
        {
            if (num % divisor == 0)
                return divisor;
            divisor +=2;
        }
        return (-1);
    }
}



int eval(std::bitset<16> x)
{

    long long p,val[9];
    for (int b=2;b<=10;b++)
    {
        long long num=0;
        for (int i=0;i<16;i++)
            num = num + (x[i]*power(b,i));
        p=chk_prime(num);
        if (p==-1)
            break;
        else
        {
            val[b-2]=p;
        }
    }
    if(p!=-1)
    {
        cout<<x;
        for (int i=0;i<9;i++)
            cout<<" "<<val[i];
        cout<<endl;
        return (-1);
    }
    return (0);
}


int main()
{
    int T,N,J;
    freopen("C-small-attempt0.in","r",stdin) ;
    freopen("cout.txt","w",stdout) ;
    cin>>T>>N>>J;
    std::bitset<16> x;
    x.reset();
    x.set(0);
    x.set(15);
    cout<<"Case #1:"<<endl;
    eval(x);
    while(x.count()!=16)
    {
        for (int i=1;i<15;i++)
        {
            if((x[i]==0))
            {
                x.flip(i);
                J = J + eval(x);
                break;
            }
                x.flip(i);

        }
        if(J==1)
            break;

    }

return 0;
}
