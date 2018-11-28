#include<bits/stdc++.h>
using namespace std;
#define ll long long
bool done[20];
void add(ll n)
{
    if(n<10)
    {
        done[n]=true;
        return;
    }
    done[n%10]=true;
    add(n/10);
    return;
}
int main()
{
    ll z,t,n,i,temp,flag,j;
    z=0LL;
    freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
    cin>>t;
    while(t--)
    {
        z++;
        for(i=0;i<=9;i++)
        {
            done[i]=false;
        }
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<z<<": INSOMNIA\n";
            continue;
        }
        for(i=1;;i++)
        {
            temp=n*i;
            add(temp);
            flag=0;
            for(j=0;j<=9;j++)
            {
                if(done[j]==false)
                {
                    flag=1;
                    break;
                }
            }
            if(!flag)
            {
                break;
            }
        }
        cout<<"Case #"<<z<<": "<<n*i<<"\n";
    }
    return 0;
}