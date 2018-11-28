#include <bits/stdc++.h>
#define ll long long int

using namespace std;

int main()
{
   freopen( "input.txt", "r", stdin );
   freopen( "output.txt", "w", stdout );
    ll t,n,i,m,temp,j=1,m1;
    cin>>t;
    while(t--)
    {
        set<int>myset;
        cin>>n;i=1;
        if(n==0)
        {
            cout<<"Case #"<<j++<<": "<<"INSOMNIA"<<endl;
            continue;
        }
        while(myset.size()!=10)
        {
            m=n*i;
            m1=m;
            while(m>0)
            {
                temp=m%10;
                myset.insert(temp);
                m/=10;
            }
            if(myset.size()==10)
                break;
            i++;
        }
        cout<<"Case #"<<j++<<": "<<m1<<endl;
    }
    return 0;
}
