#include <bits/stdc++.h>
using namespace std;

void go(long long n,long long marked[])
{
    //cout<<n<<endl;
    while(n)
    {
        long long r = n%10;
        marked[r] = 1;
        //cout<<r<<" ";
        n = n/10;
    }
    //cout<<endl;
}
long long check(long long marked[])
{
    for(long long i = 0;i<=9;i++)
    {
        if(marked[i] == 0)
            return 1;
    }
    return 0;
}
int main()
{
    long long t;
    cin>>t;
    long long c = 0;
    while(t--)
    {
        c++;
        long long n;
        cin>>n;
        if(n == 0)
        {
            cout<<"Case #"<<c<<":"<<" INSOMNIA"<<endl;
        }
        else
        {
            long long marked[20] = {0};
            long long i  = 1;

            while(check(marked))
            {
                go(i*n,marked);
                i++;
            }
            cout<<"Case #"<<c<<":"<<" "<<(i-1)*n<<endl;
        }
    }
}
