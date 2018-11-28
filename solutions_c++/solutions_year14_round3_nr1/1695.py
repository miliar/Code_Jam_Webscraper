#include<iostream>
#include<vector>
#include<cmath>
#include<cstring>
#include<fstream>
#include<cstdio>
#include<set>
#include<map>
using namespace std;

long long int gcd(long long int a,long long int b)
{
    if(a%b==0)
        return b;
    else
        return gcd(b,a%b);
}

long long int po(long long int a)
{
    long long int ret = 0;
    while(a)
    {
        ret++;
        a/=2;
    }
    return ret;
}

int main()
{
    ifstream fin("A.in");
    ofstream fout("out.txt");
    int t;
    fin>>t;
    for(int test=1;test<=t;test++)
    {
        fout<<"Case #"<<test<<": ";
        long long int p,q;
        char c;
        fin>>p;
        fin.get(c);
        fin>>q;
        long long int a = gcd(p,q);
        p/=a;
        q/=a;
        long long int ans = 0;
        double abc =  log(q)/log(2);
        if(abc != (long long int) abc)
        {
            fout<<"impossible"<<endl;
            continue;
        }
        else
        {
            fout<<po(q)-po(p)<<endl;
        }

    }
    return 0;
}
