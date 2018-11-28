#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define sl(n) scanf("%lld",&n)

int main()
{
    ifstream fin;
    ofstream fout("ans.txt");
    fin.open ("input.in");

    if(!fin.is_open())
    {
        fout<<"file error";
    }
    else
    {
        ll t;
        fin>>t;
        ll t1=t;
        while(t--)
        {
            ll k,c,s,x=1,m,n;
            fin>>k>>c>>s;
            m=pow(k,c-1);
            n=pow(k,c);
            fout<<"Case #"<<t1-t<<": ";
            while(x<=n)
            {
                fout<<x<<" ";
                x=x+m;
            }
            fout<<endl;
        }
    }
}
