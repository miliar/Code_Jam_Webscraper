#include<fstream>
#include<cstdlib>
#include<iostream>
#include<cmath>
using namespace std;

inline bool is2(long long x)
{
    return x && (!(x&(x-1)));
}

long long gcd(long long a,long long b)
{
    long long c;
    while(b)
    {
        c = b;
        b = a%b;
        a = c;
    }
    return a;
}

char buf[2000];

int main()
{
    ifstream in("asmall.in");
    ofstream out("a_output.txt");
    in.sync_with_stdio(false);
    out.sync_with_stdio(false);
    if(!in.good())
    {
        cout<<"Could not open input";
        return 0;
    }

    int t;
    long long p,q,p1,q1;
    in>>t;
    for(int x=1;x<=t;++x)
    {
        in>>buf;
        int i;
        for(i=0;buf[i]!='/';++i);
        buf[i] = 0;
        p1 = atol(buf);
        q1 = atol(buf+i+1);
        p = p1/gcd(p1,q1);
        q = q1/gcd(p1,q1);
        if(is2(q))
        {
            out<<"Case #"<<x<<": "<<(long long)(floor(log2(q)) - floor(log2(p)))<<'\n';
        }
        else
        {
            out<<"Case #"<<x<<": impossible\n";
        }

    }
    in.close();
    out.close();
    return 0;
}
