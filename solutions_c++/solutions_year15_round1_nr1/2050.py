#include <iostream>

using namespace std;

long long int A[1005];

int main()
{
    int z;
    cin>>z;
    for(int t=1; t<=z; t++)
    {
        long long int n;
        cin>>n;

        for(long long int i=1; i<=n; i++) cin>>A[i];

        long long int a=0;
        long long int b=0;

        for(long long int i=1; i<=n-1; i++)
        {
            if(A[i]>A[i+1])
            {
                a+=A[i];
                a-=A[i+1];
            }
        }

        //szukamy najwiekszej roznicy

        long long int roznica=0;
        long long int r=0;

        for(long long int i=1; i<=n-1; i++)
        {
            if(A[i]>A[i+1])
            {
                r=A[i]-A[i+1];
                if(r>roznica) roznica=r;
            }
        }

        for(long long int i=1; i<=n-1; i++)
        {
           if(A[i]>=roznica) b+=roznica;
           else b+=A[i];

        }

        cout<<"Case #"<<t<<": "<<a<<" "<<b<<endl;


    }

    return 0;
}
