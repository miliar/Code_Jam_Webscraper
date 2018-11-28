#include <bits/stdc++.h>

using namespace std;

int main()
{
    long t;
    long long n, i, m, j;
    int arr[10];

    cin>>t;
    int test = 1;
    while(t--)
    {
        memset(arr, 0, sizeof(arr));
        cin>>n;
        i = 1;
        if(n)
        while(true)
        {
            m = i*n;
            while(m)
            {
                arr[m%10]++;
                m /= 10;
            }
            for(j=0; j<10; ++j)
                if(arr[j]==0) break;
            if(j==10)
                break;
            i++;
        }
        if(n)
        cout<<"Case #"<<test<<": "<<i*n<<"\n";
        else
            cout<<"Case #"<<test<<": "<<"INSOMNIA"<<"\n";
        test++;
    }
    return 0;
}
