//Bismillahir Rahmanir Rahim
//Opu-1204026
#include<bits/stdc++.h>
using namespace std;
#define sf      scanf
#define pf      printf
#define pb      push_back
#define _       ios_base::sync_with_stdio(false);
#define ct      cin.tie(NULL);
#define ll      long long
#define eps     1e-10
#define ms(n,i) memset(n,i,sizeof n)
#define pi      2*acos(0)
#define inf     1<<30
#define fr(i,n) for(i=0;i<n;i++)
#define fr1(i,n)for(i=1;i<=n;i++)
#define nl cout<<"\n"
#define abs(x)  ((x<0)?-(x):x)
#define MAX 30005
#define sp(i)      cout<<fixed<<setprecision(i)
//STL
typedef      vector<int> vi;
typedef      vector<ll> vl;
typedef      pair<int,int>ii;
typedef      vector<ii> vii;
#define mp      make_pair
#define ft      first
#define sd      second
#define IT      iterator
#define pr(c,x) ((c).find(x)!=(c).end())
#define sz(a) int((a).size())
#define all(c)  c.begin(), c.end()
#define tr(c,i) for(typeof((c).begin()) i=(c).begin();i!=c.end();i++)
#define vpresent(c,x) (find(all(c),x)!=(c).end())

bool ck[11];
ll cn;

bool get(ll n)
{
    string s;
    stringstream ss;
    ss<<n;
    ss>>s;
    ss.clear();
    ll i;
    fr(i,s.length())
    {
        if(!ck[s[i]-'0'])
        {
            cn++;
            ck[s[i]-'0']=1;
        }
    }
    if(cn==10)return 1;
    return 0;
}


int main()
{
    //freopen("F:\\Coding\\in.txt","r",stdin);
   // freopen("F:\\Coding\\out.txt","w",stdout);
    ll t,i,n,v,z;
    sf("%lld",&t);
    fr1(z,t)
    {
        sf("%lld",&n);
      //  fr(n,1000000)
        {

        i=1;
        ms(ck,0);cn=0;
        while(i*n<=100000000&&i<=100)
        {
            v=n*i;if(get(v))break;
            i++;


        }
        if(cn==10)pf("Case #%lld: %lld\n",z,v);
        else  pf("Case #%lld: INSOMNIA\n",z);


        }

    }
    return 0;
}

