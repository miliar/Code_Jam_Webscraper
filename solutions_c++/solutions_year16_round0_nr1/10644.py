/*
akchamp
Code for fun :)
GOOGLE CODE JAM
*/
#include<bits/stdc++.h>
 
using namespace std;

#define ll             long long 
#define ld             long double
#define si(a)          scanf("%d",&a)
#define sl(a)          scanf("%lld",&a)
#define ss(a)          scanf("%s",a);                            
#define sc(a)          scanf("%c",&a);
#define pi(n)          printf("%d ",n)
#define pinl(n)        printf("%d\n",n)
#define pl(n)          printf("%lld",n)
#define plnl(n)        printf("%lld\n",n)
#define ps(n)          printf("%s",n)
#define psnl(n)        printf("%s\n",n)
#define pc(n)          printf("%c",n)
#define pcnl(n)        printf("%c\n",n)
#define f(i,a,b)       for(i=a;i<b;i++)
#define fd(i,a,b)      for(i=a;i>b;i--)
#define MOD5           100000
#define MOD7           10000000
#define MOD9           1000000000
#define PI             3.14159265358979323846
#define pb             push_back
#define mp             make_pair
#define all(n)         n.begin(),n.end()
#define fir            first
#define sec            second
#define is(a)          cout<<"Value is : "<<a<<endl

typedef vector<int> vi;
typedef pair<int,int> pi;
typedef pair<ll,ll> pl;
typedef pair<pl,ll> ppl;
typedef vector<pi> vpi;
typedef vector<ll> vl;
typedef pair<ll,ll> pl;
typedef vector<pl> vpl;
typedef vector<vi> vvi;
typedef vector<pi> vpi;
typedef map<string, int> msi;

//all(0)vector<int> v(sz,0);
ll a[10];
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    ll n,ans,i,t,x,y,flag,c;
    cin>>t;
    string s="INSOMNIA";
    c=t;
    while(t--)
    {
        cin>>n;
        memset(a,0,sizeof(a));
        flag=0;
        if(n==0)
        {
            cout<<"Case #"<<c-t<<": "<<s<<"\n";
            continue;
        }
        ans=0;
        while(ans+n<1e18)
        {
            ans+=n;
            x=ans;
            while(x>0)
            {
                y=x%10;
                x/=10;
                a[y]=1;
            }
            flag=1;
            for(i=0;i<10;i++)
            {
                if(!a[i])
                flag=0;
            }
            if(flag)
            {
                cout<<"Case #"<<c-t<<": "<<ans<<"\n";
                break;
            }
        }
        if(!flag)
        cout<<"Case #"<<c-t<<": "<<s<<"\n";
    }
    return 0;
}