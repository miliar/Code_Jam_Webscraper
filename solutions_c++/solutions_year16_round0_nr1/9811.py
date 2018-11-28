
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
int chk[20];
int cnt;

void call(int n){

    while(n != 0) {
    //cout<<n<<endl;
        if(chk[n%10] == 0) {
            cnt++;
            chk[n%10] = 1;
        }
        n/=10;
    }
}

ll pre[1000004];

void preCalculation() {

    FORL(i,1000001) {
        ll n = i;
        mem(chk,0);
        cnt = 0;
        ll mul = 1;
        ll ans = -1;
        while(cnt < 10) {
            if(ans == mul*n) {
                ans = -1;
                break;
            }
            ans = mul * n;
            call(ans);
            mul++;
        }
        pre[i] = ans;
        //cout<<pre[i]<<endl;
    }
}

int main()
{
    preCalculation();

    READ("A-small-attempt2.in");
    WRITE("out.txt");
    //ofstream fout ("ride.out");
    //ifstream fin ("ride.in");

    int t = inputI, ks = 1;

    while(t--) {
        int n = inputI;
        mem(chk,0);

        cnt = 0;
        int mul = 1;
        int ans = -1;
        int tmp;

        if(pre[n] == -1) {
            pf("Case #%d: INSOMNIA\n", ks++);
        } else {
            pf("Case #%d: %lld\n", ks++, pre[n]);
        }

    }
}




