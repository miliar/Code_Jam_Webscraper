#include<bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(false);
    long long  t;
    cin>>t;
    for(long long  i=1;i<=t;i++)
    {
        long long n;
        cin>>n;
        set<int>s;
        long long temp=n;
        if(n==0)
        {
            cout<<"Case #"<<i<<": INSOMNIA"<<"\n";
            continue;
        }
        while(temp>0)
        {
            int r=temp%10;
            s.insert(r);
            temp/=10;
        }
        if(s.size()==10)
        {
             cout<<"Case #"<<i<<": "<<n<<"\n";
             continue;
        }
        long long co=2;
        while(true)
        {
        long long temp=(co*n);
        long long temp1=(co*n);
        while(temp>0)
        {
            int r=temp%10;
            s.insert(r);
            temp/=10;
        }
        if(s.size()==10)
        {
             cout<<"Case #"<<i<<": "<<temp1<<"\n";
             break;
        }
        co++;

        }

    }

}
