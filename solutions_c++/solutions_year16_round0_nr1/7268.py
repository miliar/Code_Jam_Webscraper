#include <bits/stdc++.h>

using namespace std;

int figures (long long n, vector <long long> &c)
{
    long long k=0;
    while (n!=0)
    {
        k=n%10;
        for (int i=0; i<c.size(); i++)
        {
            if (c[i]==k) {c.erase(c.begin()+i);}
        }
        n/=10;
    }
    return c.size();
}

int main()
{
    freopen ("A-large.in", "r", stdin);
    freopen ("output.in", "w", stdout);
    long long t, b=1, z;
    cin>>t;
    vector <long long> n(t);
    vector <long long> otv(t);
    vector <long long> c(10);
    for (long long i=0; i<t; i++)
    {
        cin>>n[i];
        if (n[i]==0) otv[i]=-1;
        else
        {
            c.resize(10);
            for (long long i=0; i<10; i++)
            {
                c[i]=i;
            }
            z=n[i];
            b=1;
            while (c.size()>0)
            {
                figures(n[i], c);
                b+=1;
                n[i]=z*b;
            }
            otv[i]=n[i]-z;
        }
    }
    for (int i=0; i<otv.size(); i++)
    {
        cout<<"Case #"<<i+1<<": ";
        if (otv[i]!=-1)
        {
        cout<<otv[i]<<endl;
        }
        else cout<<"INSOMNIA"<<endl;
    }
    return 0;
}
