
/*
ID: hanifbo1
PROG: ride
LANG: C++
*/
#include<bits/stdc++.h>

using namespace std;

#define DD          double
#define INF         1000000000000000000000
#define llu            unsigned long long
#define eps         0.000001
#define FastIO      ios_base::sync_with_stdio(0); cin.tie(0)
#define READ(f)     freopen(f,"r",stdin)
#define WRITE(f)    freopen(f,"w",stdout)
#define sc          scanf
#define pf          printf
#define mem(a,val)  memset(a,val,sizeof(a))
#define rep(s,n)    for(long i=s; i<=n;i++)
#define pb          push_back
#define ll          long long
#define pi          (2*acos(0.0))
#define mx          100000
#define ssc         sscanf
#define FOR(i,n)    for(int i=1;i<=n;i++)
#define FORL(i,n)   for(int i=0;i<n;i++)
#define PQ          priority_queue
#define sr(v)       sort(v.begin(),v.end())
#define mod         1000000007
#define sz          size()
#define Case(x)     (pf("Case %ld",x);)
#define radian(x)   ((pi/180.0)*x)
#define degree(x)   ((180.0/pi)*x)
#define inputI      ({ long tt2; sc("%ld",&tt2); tt2;})
#define inputD      ({DD a; sc("%lf",&a); a;})
#define VI          vector<int>


long GCD(long a,long b)
{
    if(b==0)return a;

    return GCD(b,a%b);
}

/*bool prime[mx+5];
vector<long>v;

void sieve()
{
    for(long i=4;i<=mx; i=i+2)
    prime[i]=1;

    for(long i=3; i*i<=mx;i=i+2)
    {
        if(prime[i] == 0)
        {
            for(long j=2*i; j<=mx; j=i+j)
            prime[j]=1;
        }
    }


    v.pb(2);
    for(long i=3;i<=mx;i=i+2)
    {
        if(prime[i]==0)
        v.pb(i);
    }
}*/


long long bigMod(long long b,long long p, long long m)
{
    //cout<<"eee"<<endl;
    if(b == 1)
        return b;
    if(p == 0 )return 1;
    if( p == 1)return b;
    if(p%2 == 0)
    {
        ll temp = bigMod(b,p/2,m);
        return (temp*temp)%m;
    }
    else
        return (b  *  bigMod(b,p-1,m))%m;
}


ll modInverse(ll a,ll m)
{


    return bigMod(a,m-2,m);

}

string str;

int main()
{

    READ("B-large.in");
    WRITE("out.txt");
    //ofstream fout ("ride.out");
    //ifstream fin ("ride.in");
    int t = inputI, ks = 1;

    while(t --) {

        cin>>str;
        string tmp = str;
        int len = str.length()-1;
        int ans = 0;
        char off = str[len];

        while(len >= 0) {
            if(tmp[len] == off) {
                len--;
            } else {
                ans++;
                for(int i = len; i>=0; i--){
                    if(tmp[i] == '+')tmp[i] = '-';
                    else tmp[i] = '+';
                }
            }
        }
        if(tmp[0] == '-')ans++;
        pf("Case #%d: %d\n",ks++,ans);
    }
}




