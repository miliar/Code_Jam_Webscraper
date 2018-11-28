#include<bits/stdc++.h>
#define ll long long
#define ff first
#define ss second
#define m_p make_pair
#define pb push_back
#define pf push_front
#define ppf pop_front
#define ppb pop_back
#define NINF 0x80
#define INF 0x3f
#define eps 1e-9
#define l_b lower_bound
#define u_b upper_bound
#define MOD1 1000000007
#define MOD2 1000000009
#define check(n,pos) (bool)(n & (1<<pos))
#define biton(n,pos) (n | (1<<pos))
#define bitoff(n,pos) (n & ~(1<<pos))
using namespace std;
string s;
bool cut[1100];
int sz;
inline int cutoff(int n)
{
    int cutted=0;
    for(int i=n; i>=0; i--)
    {
        if(cut[i]) break;
        cut[i]=1;
        cutted+=(s[i]-'0');
    }
    return cutted;
}
int main()
{
    int ks,kase;
    freopen("A-large.in","r",stdin);
    freopen("outputa.txt","w",stdout);
    cin>>kase;
    for(ks=1; ks<=kase; ks++)
    {
        memset(cut,0,sizeof cut);
        cin>>sz>>s;
        sz+=1;
        int totcut=s[0]-'0',ans=0;
        cut[0]=1;
        while(totcut<sz)
        {
            int ret=cutoff(totcut);
            //cout<<totcut<<" "<<ret<<endl;
            if(ret==0)
            {
                ans++;
                totcut++;
            }
            else totcut+=ret;
        }
        cout<<"Case #"<<ks<<": "<<ans<<endl;
    }
}
