#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;int i=1;
    while(t--)
    {
        long long int n;
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<i<<": INSOMNIA\n";
        }
        else
        {
        long long int a[10];
        memset(a,0,sizeof(a));
        long long int b=0;
        long long int c=0;
        while(c<10)
        {
            b++;
            long long int k=n*b;
            while(k>0)
            {
                int r=k%10;
                if(a[r]==0)
                {
                    a[r]=1;
                    c++;
                }
                k=k/10;
            }
        }cout<<"Case #"<<i<<": "<<n*(b)<<"\n";}
    }
}
