#include<bits/stdc++.h>
#define ll long long int
#define PB push_back
#define F first
#define S second
#define tr(c,i) for(typeof((c).begin())i = (c).begin(); i != (c).end(); i++) 
#define sint(n); scanf("%d",&n);
#define sll(n); scanf("%lld",&n);
#define pint(n); printf ("%d\n",n);
#define pll(n); printf ("%lld\n",n);
#define sst(n); scanf("%s",n);
#define pst(n); printf ("%s\n",n);
#define f(i,a,b) for(ll i=a;i<b;i++)
#define set(a,b) memset(a, b, sizeof(a))


using namespace std;

char s[1005];
char ans[50000];
ll st,en;

int before(ll x)
{
    ll ret;
    if (x==0)
        ret=1;
    else
    {
        //cout<<(s[x])<<(ans[st])<<endl;
        //ll t1=s[x], t2=ans[st];
        //cout<<t1<<" "<<t2<<endl;
        if (s[x]>=ans[st])
            ret=1;
        else
            ret = 0;
    }
    //cout<<ret<<endl;
    return ret;
}

int main()
{
    ll test;
    cin>>test;
    f(t,1,test+1)
    {
        sst(s);
    ll len = strlen(s);
    st=en=25000;
    f(i,0,len)
    {
        if (i==0)
            ans[st]=s[i];
        else if (before(i)==1)
            ans[--st]=s[i];
        else
            ans[++en]=s[i];
    }
    cout<<"Case #"<<t<<": ";
    f(i,st,en+1)
    {
        cout<<ans[i];
    }
    cout<<endl;
    }
    return 0;
}
