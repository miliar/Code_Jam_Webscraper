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
    freopen("output.txt", "w", stdout);
    long long int t;
    cin>>t;
    long long int cases = t;
    for(long long int i=0;i<t;i++)
    {
        string a,b;
        cin>>a;

        long long int k=0;
        for(long long int j=0;j<a.length();j++)
        {   
            if(j==0)
                b=b+a[j];
            else
            {
                if(a[j]>=b[0])
                    b=a[j]+b;
                else
                    b=b+a[j];
            }
        }
        cout<<"Case #"<<i+1<<": "<<b;
        if(cases-i+1)
        cout<<endl;
    }
    return 0;
}