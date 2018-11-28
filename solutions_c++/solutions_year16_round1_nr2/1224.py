#include <bits/stdc++.h>
using namespace std;
int main()
{
    long long t;
    cin>>t;
    long long coun = 0;
    long long m[10000]= {0};
    while(t--)
    {
        coun++;
        long long n;
        cin>>n;
        for(long long i = 1;i<= 2*n-1;i++)
        {
            for(long long j = 0;j< n;j++)
            {
                long long nmn;
                cin>>nmn;
                m[nmn]++;
            }
        }
        long long arr[2600];
        long long id = 0;
        for(long long i = 1;i<=2500;i++)
        {
            if(m[i]%2 == 1)
                arr[id++] = i;
        }
        sort(arr,arr+id);
        cout<<"Case #"<<coun<<": ";
        for(long long i = 0;i< id;i++)
        {
            if(i)
            cout<<" ";
            cout<<arr[i];
        }
        cout<<endl;
    }

}
