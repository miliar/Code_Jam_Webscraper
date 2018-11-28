/////////////////////// All Is Well /////////////////////////

#include <bits/stdc++.h>

#define FOR(i, s, e) for(int i=s; i<e; i++)
#define loop(i, n) for(int i=0; i<n; i++)
#define CIN   ios_base::sync_with_stdio(0); cin.tie(0)
#define getint(n) scanf("%d", &n)
#define pb(a) push_back(a)
#define ll long long int
#define ull unsigned long long int
#define dd double
#define SZ(a) int(a.size())
#define read() freopen("input.txt", "r", stdin)
#define write() freopen("output.txt", "w", stdout)
#define mem(a, v) memset(a, v, sizeof(a))
#define all(v) v.begin(), v.end()
#define pi acos(-1.0)
#define pf printf
#define sf scanf
#define mp make_pair
#define paii pair<int, int>
#define padd pair<dd, dd>
#define pall pair<ll, ll>
#define fr first
#define sc second
#define CASE(n) printf("Case #%d:\n",++n)
#define CASE_COUT cout<<"Case "<<++cas<<": "
#define inf 1000000000
#define EPS 1e-9

using namespace std;

//8 way moves
//int fx[]={0,0,1,-1,1,1,-1,-1};
//int fy[]={1,-1,0,0,1,-1,1,-1};

//knight moves
//int fx[]={-2,-2,-1,-1,1,1,2,2};
//int fy[]={-1,1,-2,2,-2,2,-1,1};

//Bit operation
int SET(int n,int pos){ return n=n | (1<<pos);}
int RESET(int n,int pos){ return n=n & ~(1<<pos);}
int CHECK(ll n,int pos){ return (bool) (n & (1LL<<pos));}


int bigMod(int n,int power,int MOD)
{
    if(power==0)
        return 1;
    if(power%2==0)
    {
        int ret=bigMod(n,power/2,MOD);
        return ((ret%MOD)*(ret%MOD))%MOD;
    }
    else return ((n%MOD)*(bigMod(n,power-1,MOD)%MOD))%MOD;
}

int modInverse(int n,int MOD)
{
    return bigMod(n,MOD-2,MOD);
}

ll POW(ll x, ll y)
{
    ll res= 1;
    for ( ; y ; ) {
        if ( (y&1) ) {
            res*= x;
        }
        x*=x;
        y>>=1;
    }
    return res;
}

int inverse(int x)
{
    dd p=((dd)1.0)/x;
    return (p)+EPS;
}

int gcd(int a, int b)
{
    while(b) b^=a^=b^=a%=b;
    return a;
}

int nC2(int n)
{
    return n*(n-1)/2;
}

int MOD(int n,int mod)
{
    if(n>=0)
        return n%mod;
    else if(-n==mod)
        return 0;
    else
        return mod+(n%mod);
}

ll n,cnt;
vector<ll>data;

ll findDiv(ll xx)
{
    for(ll i=2;i<=sqrt(xx);i++)
    {
        if(xx%i==0)
            return i;
    }
    return -1;
}
//
ll convert(ll xx,ll i)
{
    ll val=0;
    for(ll j=0;j<n;j++)
    {
        if(CHECK(xx,j)==1)
        {
            val+=POW(i,j);
        }
    }
    return val;
}
//
//int call(ll i,ll mask)
//{
//    if(i>=n-1)
//    {
//        if(cnt==50)
//            return 0;
//        cout<<mask<<endl;
//        int ff=0;
//        for(ll j=2;j<=10;j++)
//        {
//            ll xx=convert(mask,j);
//            ll pp=findDiv(xx);
//            if(pp==-1)
//                ff=1;
//            cout<<pp<<" ";
//        }
//        if(ff==0)
//        {
//            data.pb(mask);
//            cnt++;
//        }
//        cout<<endl;
//        return 0;
//    }
//    call(i+1,SET(mask,i));
//    call(i+1,mask);
//}


void print_base(ll xx)
{
    for(int i=n-1;i>=0;i--)
    {
        if(CHECK(xx,i))
            pf("1");
        else
            pf("0");
    }
}

int main()
{
    read();
    write();
    data.pb(65535);
    data.pb(49151);
    data.pb(40959);
    data.pb(61439);
    data.pb(45055);
    data.pb(53247);
    data.pb(47103);
    data.pb(55295);
    data.pb(59391);
    data.pb(34815);
    data.pb(64511);
    data.pb(48127);
    data.pb(56319);
    data.pb(39935);
    data.pb(60415);
    data.pb(62463);
    data.pb(37887);
    data.pb(50175);
    data.pb(65023);
    data.pb(48639);
    data.pb(56831);
    data.pb(60927);
    data.pb(36351);
    data.pb(62975);
    data.pb(38399);
    data.pb(58879);
    data.pb(42495);
    data.pb(50687);
    data.pb(63999);
    data.pb(39423);
    data.pb(43519);
    data.pb(51711);
    data.pb(45567);
    data.pb(57855);
    data.pb(33279);
    data.pb(65279);
    data.pb(48895);
    data.pb(57087);
    data.pb(61183);
    data.pb(44799);
    data.pb(63231);
    data.pb(38655);
    data.pb(59135);
    data.pb(50943);
    data.pb(34559);
    data.pb(64255);
    data.pb(60159);
    data.pb(43775);
    data.pb(51967);
    data.pb(35583);

	int t,cas=0;
	getint(t);
	while(t--)
    {
        ll j;
        cin>>n>>j;
        CASE(cas);
        loop(i,j)
        {
            print_base(data[i]);
            for(ll kk=2;kk<=10;kk++)
            {
                ll xx=convert(data[i],kk);
                pf(" %lld",findDiv(xx));
            }
            pf("\n");
        }
    }
	return  0;

}
