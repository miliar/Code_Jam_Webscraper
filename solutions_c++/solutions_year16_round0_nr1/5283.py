#include<bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(false);
    long long t;
    cin>>t;
    long long i=0;
    while(t--)
    {
        i++;
        long long n,no;
        cin>>no;
        if(no==0)
            cout<<"Case #"<<i<<": INSOMNIA\n";
        else
        {
           set<long long> s;
           long long sum=0;
            while(s.size()!=10)
            {
                  sum+=no;
                 long long n=sum;
                while(n!=0)
                {
                    long long d=n%10;
                    n/=10;
                    s.insert(d);
                }

            }
           cout<<"Case #"<<i<<": "<<sum<<"\n";
        }
    }

}
