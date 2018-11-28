#include<iostream>
#include<sstream>
#include<math.h>
#include<string.h>
using namespace std;

int main()
{
    unsigned int T;
    unsigned long long int radius, volume, sum, count;
    cin>>T;
    for (int i=0;i<T;i++)
    {
        cin>>radius>>volume;
        sum=0;
        count=0;
        for (unsigned long long int ctr=1;sum<=volume;ctr=ctr+4)
        {
            sum = sum + 2*radius + ctr;
            count++;
        }
        cout<<"Case #"<<i+1<<": "<<count-1<<"\n";
    }
    return 0;
}
