#include <iostream>
#include <vector>

using namespace std;

#define ull unsigned long long

ull convert(ull n, ull b)
{
    vector<ull> v;
    while(n)
    {
        ull d=n%10;
        v.push_back(d);
        n/=10;
    }

    ull a=0;
    n=1;
    for(ull i=0;i<v.size();i++)
    {
        a+=n*v[i];
        n*=b;
    }

    return a;
}

ull convert2(ull n)
{
    vector<ull> v;
    while(n)
    {
        ull d=n%2;
        v.push_back(d);
        n/=2;
    }

    ull a=0;
    while(v.size())
    {
        a=a*10+v[v.size()-1];
        v.pop_back();
    }

    return a;
}

ull factor(ull n)
{
    if(n%2==0)
        return 2;

    for(ull i=3;i*i<=n;i++)
        if(n%i==0)
            return i;

    return 1;
}

bool isPrime(ull n)
{
    if(n%2==0 && n!=2)
        return false;

    for(ull i=3;i*i<=n;i++)
        if(n%i==0)
            return false;

    return true;
}

int main() {

    ull T,N,J;
    cin>>T;
    for(ull t=1;t<=T;t++) {
        cout<<"Case #"<<t<<":\n";
        cin >> N >> J;

        ull n = 1 << (N-1);
        n++;

        while(J)
        {
            bool flag=true;
            ull p=convert2(n);
            for(ull i=2;i<=10;i++)
            {
                if(flag)
                {
                    ull m=convert(p,i);
                    flag=!isPrime(m);
                }
            }

            if(flag)
            {
                J--;
                cout << p << " ";
                for(ull i=2;i<=10;i++)
                {
                    if(flag)
                    {
                        ull m=convert(p,i);
                        ull f=factor(m);
                        cout<<f<<" ";
                    }
                }
                cout<<endl;
            }
            n+=2;
        }
    }

    return 0;
}