#include <bits/stdc++.h>
#define IOS ios::sync_with_stdio(0);
using namespace std;
set<long long> tmp;
long long n;
 long long i;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    IOS
    int cases,c=1;
    cin>>cases;
    while(cases--)
    {
        cin>>n;
        cout<<"Case #"<<c<<": ";
        if(n==0)cout<<"INSOMNIA"<<endl; else
        {
        i=1;
        while(tmp.size()<10)
        {
            long long m = n*i;
            while(m>0)
            {
                   tmp.insert(m%10);
                   m/=10;
            }
            ++i;
        }
        cout<<(n)*(i-1)<<endl;
        tmp.clear();
        }
        ++c;
    }
}
