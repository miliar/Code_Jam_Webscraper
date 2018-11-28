#include<bits/stdc++.h>

using namespace std;

#define s(n) scanf("%lld", &n)

int main()
{
    long long int T, N;
    s(T);
    long long int counter=1, prod;
    while(T--)
    {
        long long int arr[10];
        for(long long int i=0;i<10;i++)
            arr[i]=0;
        s(N);
        for(long long int i=1;i<=100000000;i++)
        {
            long long int t=N*i;
            while(t>0)
            {
                arr[t%10]++;
                t=t/10;
            }
            prod=arr[0];
            for(long long int ij=1;ij<10;ij++)
                prod*=arr[ij];
            if(prod!=0)
            {
                printf("Case #%d: %d\n",counter, N*i);
                break;
            }
        }
        if(prod==0)
            printf("Case #%d: INSOMNIA\n", counter);
        counter++;
    }
    return 0;
}
