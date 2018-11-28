#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
map<ll,int>memo;
void mark(ll n)
{
    while(true)
    {
        ll rem=n%10;
        memo[rem]++;
        n/=10;
        if(n==0)
            return;
    }
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int test;
    cin>>test;
    for(int x=1;x<=test;x++)
    {
        ll n,m;
        cin>>n;
        m=n;
        memo.clear();
        cout<<"Case #"<<x<<": ";
        bool found=false;
        for(int i=0;i<1000000;i++)
        {
            mark(n);
            bool flag=true;
            for(ll i=0;i<10;i++)
            {
                if(memo[i]==0)
                {
                    flag=false;
                    break;
                }
            }
            if(flag)
            {
                found=true;
                cout<<n<<endl;
                break;
            }
            n+=m;
        }
        if(!found)
            cout<<"INSOMNIA"<<endl;
    }
    fclose(stdout);
}
