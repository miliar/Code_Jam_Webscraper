// #CodeLikeTheMartian
#include <bits/stdc++.h>

#define     MOD       1000000007
#define     mp(a,b)   make_pair(a,b)
#define     pb        push_back
#define     lb        lower_bound
#define     ub        upper_bound
#define     SIZE      1000001
#define     MAX       INT_MAX
#define     fi        first
#define     se        second
#define     fastInput ios::sync_with_stdio(false); cin.tie(0);
using namespace std;

typedef long long int  ll;
typedef long double ld;
typedef unsigned int uint;
typedef unsigned long long int ull;
ll pp[10][17];
ll N,J;
inline void pre()
{
    for(ll i=2;i<=10;++i)
    {
        for(ll j=0;j<=16;++j)
        {
            pp[i][j]=ceil(pow(i,j));
        //    cout<<pp[i][j]<<" ";
        }
       // cout<<endl;
    }
}
inline ll isPrime(ll n)
{
	if(n<=1)
	       return 1;
	for(ll i=2;i*i<=n;++i)
		if(n%i==0)
            return i;
	return 1;
}
vector<int> fact(ll n)
{
    vector<int> tt;
    for(ll i=2;i<=10;++i)
    {
        ll tmp=0;
        for(int j=N-1;j>=0;--j)
        {
            if(n&(1LL<<j))
                tmp+=ceil(pow(i,j));

        }

        int res=isPrime(tmp);
        if(res==1)
        {
            tt.clear();
             return tt;
        }
        tt.pb(res);
    }
    return tt;
}
int main()
{
    int T;
    cin>>T;
    cin>>N>>J;
    int last=(1LL<<N);
    int cnt=0;
    cout<<"Case #1:"<<endl;
    int res=(1LL<<(N-1));
    for(int i=(1LL<<(N-1));i<last;++i)
    {
        if(i&1)
        {
            vector<int> tt=fact(i);
            if(tt.size()>0)
            {
                ++cnt;
                for(int j=N-1;j>=0;--j)
                {
                     cout<<(i&(1LL<<j) ? '1' :'0');
                }
                cout<<" ";
                for(int j=0;j<tt.size();++j)
                {
                    cout<<tt[j]<<" ";
                }
               cout<<endl;
            }
        }
        if(cnt==J)
            break;
    }

    return 0;
}
