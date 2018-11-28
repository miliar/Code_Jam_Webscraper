#include <iostream>
#include <vector>
#include <stdio.h>
#include <string.h>
#include <queue>
#include <stdio.h>
#include <sstream>

using namespace std;
int dig[10]={0};
int num = 10;



bool finished(long long k)
{
    while (k!=0)
    {
        long long m = k % 10;
        if(dig[m] == 0)
        {
            dig[m]=1;
            num--;
        }
        k = k/10;
    }

    if (num==0)
        return true;
    return false;
}
void solve(long long k, long long i)
{

    long long j = 1;
    long long kk = k;
    while(true)
    {
        kk = k*j;

        if(finished(kk))
        {
            cout<<"Case #"<<i<<":"<<" "<<kk<<endl;
            break;
        }
        j++;
    }
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    long long t;
    cin>> t;
    for(long long i = 1; i<=t; i++)
    {
        long long k;
        cin>> k;

        if(k == 0)
        {
            cout<<"Case #"<<i<<":"<<" "<<"INSOMNIA"<<endl;
        }
        else
            solve(k,i);

        num=10;
        dig[0] = 0; dig[1] = 0; dig[2] = 0; dig[3] = 0; dig[4] = 0;
        dig[5] = 0; dig[6] = 0; dig[7] = 0; dig[8] = 0; dig[9] = 0;

    }
    return 0;
}
