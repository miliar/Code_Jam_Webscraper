#include<bits/stdc++.h>
#define ll long long
#define pb push_back
#define mp make_pair
using namespace std;
ll a[11];
int f1(ll num)
{
    ll temp = num;
    while(temp>0)
    {
        ll rem = temp%10;
        a[rem]+=1;
        temp=temp/10;
    }
    for(int i=0;i<10;i++)
    {
        if(a[i]<=0)
            return 0;
    }
    return 1;
}

int main()
{
    freopen("A-large (2).in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,q=0;
    cin>>t;
    while(t--)
    {
        q++;
        ll n;
        cin>>n;
        for(int i=0;i<10;i++)
            a[i]=0;
        if(n==0)
            cout<<"Case #"<<q<<": "<<"INSOMNIA"<<"\n";
        else
        {
            int i;
            int flag = 0;
            ll ans;
            for(i=1;;i++)
            {
                ll num = i*n;
                flag=f1(num);
                if (flag==1)
                {
                    cout<<"Case #"<<q<<": "<<num<<"\n";
                    break;
                }
                if(i>1000)
                {
                    cout<<"Case #"<<q<<": "<<"INSOMNIA"<<"\n";
                    break;
                }
            }
        }
    }
    return 0;
}
