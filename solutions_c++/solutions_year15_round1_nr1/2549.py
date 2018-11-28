#include <iostream>
using namespace std;

int main()
{
    long long t;
    cin >>t;
    while(t--)
    {
        long long n,s=0;
        cin >>n;
        long long a[n];
        long long max=0,diff=0;
        for(int i=0;i<n;i++)
        {
            cin >> a[i];
            if(i==0)
            continue;
            if(a[i]<a[i-1])
            {
            s=s+a[i-1]-a[i];
            diff=a[i-1]-a[i];
            if(diff>max)
            max=diff;
            }
        }
        long long p=0;
        for(long long i=0;i<n-1;i++)
        {
                if(a[i]<=max)
                p=p+a[i];
                else
                {
                    p=p+max;
                }
        }
    
        cout<<s<<" "<<p<<endl;
    }
    return 0;
}
            