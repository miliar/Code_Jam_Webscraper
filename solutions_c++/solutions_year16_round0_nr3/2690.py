#include<bits/stdc++.h>
using namespace std;
#define gc getchar
#define ll long long
#define v vector
#define pr pair<int,int>
#define sd second
#define ft first
#define pb push_back
#define mp make_pair
ll isnotprime(ll n)
{
//    cout<<n<<endl;
    ll i;
    int flag=0;
    for(i=2;i<=sqrt(n);i++)
    {
        if(n%i==0)
            {flag=1;
        break;}
    }
    if(flag==0)
        i=0;
    return i;
}
ll power(ll n,ll i)
{
    if(i==0)
        return 1LL;
    ll t=power(n,i/2);
    t=t*t;
    if(i%2)
        return t*n;
    else
        return t;
}
void print(int n,int b)
{
    int x;
    x=n;
    int i=0;
    int a[b];
    while(i<b)
    {
        if(x&1)
            a[i]=1;
        else
            a[i]=0;
        x=x>>1;
        i++;
    }
    for(i=b-1;i>=0;i--)
        cout<<a[i];
    cout<<" ";
}
int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("output.txt","w",stdout);
    ios::sync_with_stdio(false);
    int i,j,k,t,n,flag,x,ans,c,p,b,num,temp;
    cin>>t;
    cin>>b>>n;
    c=0;
    i=1;
    num=0|(1<<(b-1));
    num=num|1;
    cout<<"Case #1:"<<endl;
    while(c<n)
    {
        ll a[11]={0};
        temp=i<<1;
        temp=temp|num;
        x=temp;
        p=0;
        while(x!=0)
        {
            if(x&(1))
            {
                for(j=2;j<=10;j++)
                {
                    a[j]+=power(j,p);
                }
            }
            x=x>>1;
            p++;
        }
        for(j=2;j<=10;j++)
        {
            if((a[j]=isnotprime(a[j]))==0)
                break;
        }
        if(j==11)
        {
            c++;
            print(temp,b);
            for(j=2;j<=10;j++)
                cout<<a[j]<<" ";
            cout<<endl;
        }
        i++;
    }
    return 0;
}
