#include <iostream>
#include <string.h>
#include <set>
#include <cstring>
#include <cmath>

using namespace std;

set<long long int> sett1;

long long int flagger=0;

void ans(long long int n)
{
    while(n)
    {
        sett1.insert(n%10);
        n=n/10;
    }
    if(sett1.size()==10)
    flagger=1;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("outerrr.in", "w", stdout);
    long long int t;
    cin>>t;
    long long int cases = t;
    while(t--)
    {   
        long long int n;
        cin>>n;
        if(n==0)
            cout<<"Case #"<<cases-t<<": "<<"INSOMNIA"<<endl;
        else
        {
            long long int i=1;
            flagger=0;
            while(1)
            {
                ans(n*i);
                i++;
                if(flagger==1)
                    break;
            }
            cout<<"Case #"<<cases-t<<": ";
            cout<<n*(i-1)<<endl;
        }
        sett1.clear();
    }
    return 0;
}