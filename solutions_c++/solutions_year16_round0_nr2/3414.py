#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long t;
    cin>>t;
    long long c = 0;
    while(t--)
    {

        c++;
        string s;
        cin>>s;
        long long ans=0;
        long long len = s.length();
        long long i= 0;
        long long f = 0;
        while(i<len)
        {
            while(s[i]=='+' && i<len)
                {
                    f =1;
                    i++;
                }
                long long i_copy = i;
            while(s[i]=='-' && i < len)
                {
                    i++;

                }
                if(i != i_copy)
                {
                    if(f)
                    ans++;
                    ans++;
                }

        }

        cout<<"Case #"<<c<<": "<<ans<<endl;




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
