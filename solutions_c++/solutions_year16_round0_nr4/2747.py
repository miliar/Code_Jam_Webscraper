#include <bits/stdc++.h>
using namespace std;
long long powe(long long k,long long c)
{
    if(c == 0)
    return 1;
    long long kcop = k;
    for(long long i = 2;i<=c;i++)
    {
        kcop*=k;
    }
    return kcop;
}
int main()
{
    long long t;
    cin>>t;
    long long co = 0;
    while(t--)
    {
        co++;
        long long k,c,s;
        cin>>k>>c>>s;
        long long nmn = powe(k,c-1);


        cout<<"Case #"<<co<<":";
        long long i = 1;
        while(s--)
        {
            cout<<" ";
            cout<<i;
            i+=nmn;
        }
        cout<<endl;



    }
}
/*
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
long long main()
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
            long long loop = 10;
            while(loop--)
            {
                go(i*n,marked);
                i++;
            }
            for(long long i = 0;i<=9;i++)
            {
                if(marked[i] == 0)
                {
                    cout<<i<<endl;
                }
            }
        }
    }
}*/
