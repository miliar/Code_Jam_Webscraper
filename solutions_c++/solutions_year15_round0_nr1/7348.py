#include<iostream>
#include<stdio.h>
#include<cmath>
using namespace std ;

//int* form (int Smax, long long K);

long long chk (int *p,int Smax);

main()
{
    int T;
    freopen("A-large.in","r",stdin) ;
    freopen("aout.txt","w",stdout) ;
    cin>>T;
    long long X[T];
    for (int i=0;i<T;i++)
    {
        char K;
        int Smax;
        cin>>Smax;
        int H[Smax+1];
        for (int i=0;i<=Smax;i++)
        {
            cin>>K;
            H[i] = K - '0';
        }

        //int *p;
        //p = form (Smax,K);
        X[i] = chk (H,Smax);
    }
    for (int i=0;i<T;i++)
        cout <<"Case #"<<i+1<<": "<<X[i]<<endl;
}

/*int* form (int Smax, long long K)
{
    int A[Smax+1];
    for (int i=Smax;i>=0;i--)
    {
        A[i-Smax]= K / (pow(10,i));
        K = K % (long(pow(10,i)));
    }
    return A;
}*/

long long chk (int A[],int Smax)
{
    long long z = A[0],cnt=0;
    for (int i = 1; i<=Smax; i++)
    {
        if (z < i)
        {
            cnt += (i-z);
            z += (i-z);
        }
        z += A[i];
    }
    return cnt;
}
