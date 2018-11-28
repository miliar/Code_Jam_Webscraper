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
#define CASE(n) printf("Case #%d: ",++n)
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
int SET(int n,int pos)
{
    return n=n | (1<<pos);
}
int RESET(int n,int pos)
{
    return n=n & ~(1<<pos);
}
int CHECK(int n,int pos)
{
    return (bool) (n & (1<<pos));
}


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

int POW(int x, int y)
{
    int res= 1;
    for ( ; y ; )
    {
        if ( (y&1) )
        {
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

int main()
{
//    read();
//    write();
    int t,cas=0;
    getint(t);
    while(t--)
    {
        string ss;
        cin>>ss;
        map<char,int>mapa;
        int sz=ss.size();
        loop(i,sz)
        {
            mapa[ss[i]]++;
        }
        string ans="";
        while(1)
        {
            if(mapa['Z'])
            {
                mapa['Z']--;
                mapa['E']--;
                mapa['R']--;
                mapa['O']--;
                ans+='0';
            }
            else
                break;
        }
        while(1)
        {
            if(mapa['U'])
            {
                mapa['F']--;
                mapa['U']--;
                mapa['R']--;
                mapa['O']--;
                ans+='4';
            }
            else
                break;
        }
        while(1)
        {
            if(mapa['G'])
            {
                mapa['E']--;
                mapa['I']--;
                mapa['G']--;
                mapa['H']--;
                mapa['T']--;
                ans+='8';
            }
            else
                break;
        }
        while(1)
        {
            if(mapa['W'])
            {
                mapa['T']--;
                mapa['W']--;
                mapa['O']--;
                ans+='2';
            }
            else
                break;
        }
        while(1)
        {
            if(mapa['X'])
            {
                mapa['S']--;
                mapa['I']--;
                mapa['X']--;
                ans+='6';
            }
            else
                break;
        }
        while(1)
        {
            if(mapa['H'])
            {
                mapa['T']--;
                mapa['E']-=2;
                mapa['H']--;
                mapa['R']--;
                ans+='3';
            }
            else
                break;
        }
        while(1)
        {
            if(mapa['O'])
            {
                mapa['O']--;
                mapa['N']--;
                mapa['E']--;
                ans+='1';
            }
            else
                break;
        }
        while(1)
        {
            if(mapa['F'])
            {
                mapa['F']--;
                mapa['E']--;
                mapa['I']--;
                mapa['V']--;
                ans+='5';
            }
            else
                break;
        }
        while(1)
        {
            if(mapa['S'])
            {
                mapa['S']--;
                mapa['E']-=2;
                mapa['V']--;
                mapa['N']--;
                ans+='7';
            }
            else
                break;
        }
        while(1)
        {
            if(mapa['N']>=2)
            {
                mapa['N']-=2;
                mapa['E']--;
                mapa['I']--;
                ans+='9';
            }
            else
                break;
        }
        sort(all(ans));
        CASE(cas);
        cout<<ans<<endl;
    }
    return  0;

}
