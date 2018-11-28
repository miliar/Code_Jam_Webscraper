#include <bits/stdc++.h>
#define MOD 1000000007
using namespace std;

long long ar[1000002];
set<long long> st;

int main()
{
    freopen("inp.txt","r",stdin);
    freopen("op.txt","w",stdout);
    ios::sync_with_stdio(false);
    cin.tie(0);
    long long n,m,a,b,i,j,val=0,ans=0,x,y,t,T;
    cin>>T;
    for(t=1;t<=T;t++)
    {
        cin>>n;
        st.clear();
        i=n;
        x=n;
        if(n==0)
        {
            cout<<"Case #"<<t<<": "<<"INSOMNIA\n";
            continue;
        }
        while(st.size()<10)
        {
            j=i;
            while(j)
            {
                st.insert(j%10);
                j/=10;
            }
            i+=x;
        }
        cout<<"Case #"<<t<<": "<<i-x<<"\n";
    }
}