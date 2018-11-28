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
bool vis[11];

int cnt;
ll rem(ll n)
{
    while(n>0)
    {
        if(!vis[n%10])
        {
            vis[n%10]=true;
            --cnt;
        }
        n/=10;
    }
    return cnt;
}
int main()
{
    int T;
    cin>>T;
    for(int t=1;t<=T;++t)
    {
        string s;
        ll N;
        cin>>N;
        //int cnt[11];

        for(int i=0;i<11;++i)
            vis[i]=false;
        cnt=10;
        ll ans=N;
        ll mm=1;
        if(N>0)
        {

            while(1)
            {
                if(rem(N*mm)==0)
                    break;
                ++mm;
            }
        }
        ans=N*mm;
        if(ans==0)
            cout<<"Case #"<<t<<": "<<"INSOMNIA"<<endl;
        else
            cout<<"Case #"<<t<<": "<<ans<<endl;
    }
	return 0;
}

