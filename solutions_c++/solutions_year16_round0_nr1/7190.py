#include<bits/stdc++.h>
using namespace std;
#define ll long long
set <ll> s;
int main()
{

freopen("input.in","r",stdin);
freopen("output.txt","w",stdout);
ll t,n,k,temp,temp2,ans;
cin>>t;

for(k=1;k<=t;k++)
{
    s.clear();
    cin>>n;
    temp=n;
    if(n==0)
    {
        cout<<"Case #"<<k<<": INSOMNIA\n";
        continue;
    }

    while(s.size()!=10)
    {
        temp2=temp;
        while(temp2>0)
        {
            s.insert(temp2%10);
            temp2/=10;
        }
        temp+=n;
    }
    cout<<"Case #"<<k<<": "<<temp-n<<"\n";

}

return 0;
}
