#include<iostream>

using namespace std;

int main()
{
    long long count=0;
    long long a,b,k,n;

    cin>>n;
    for(long long t=1;t<=n;t++)
    {
        long long x[10000]={0};
        cin>>a>>b>>k;
        count = 0;
        for(long long i=0;i<a;i++)
        {
            for(long long j=0;j<b;j++)
            {

                x[i&j]++;
            }
        }
        for(long long i=0;i<k;i++)
        {
            count+=x[i];
        }
        cout<<"Case #"<<t<<": "<<count<<endl;

    }

    return 0;
}
