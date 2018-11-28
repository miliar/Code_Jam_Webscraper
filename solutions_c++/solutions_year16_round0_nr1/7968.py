#include<bits/stdc++.h>

using namespace std;

#define sf scanf
#define pf printf
#define ll long long
#define fr(I,M,N) for(I=M;I<=N;I++)
#define fr_(I,M,N) for(I=M;I>=N;I--)
#define re return
#define sfn cin>>n
#define bal pf("bal\n")
#define pb push_back
#define ins insert
#define sz(X) X.size()
#define xx first
#define yy second
#define cont continue
#define memo(X,N) memset(X,N,sizeof(X))
#define all(X) X.begin(),X.end()

/*int pr[100000],prnum[1000001];

void sieve()
{
    int i,j;
    for(i=1;i<=1000000;i++)
        prnum[i]=i+1;
    for(i=1;i<=1000000;i++)
        if(prnum[i]!=-1)
            for(j=2*prnum[i]-1;j<=1000000;j+=prnum[i])
                    prnum[j]=-1;
    j=1;
    for(i=1;i<=1000000;i++)
        if(prnum[i]!=-1)
            pr[j++]=prnum[i];
}*/

/*ll m_ncr[10001][10001];
ll ncr(ll i,ll j)
{
    if(j==1) re i;
    if(i==j) re 1;
    if(m_ncr[i][j]!=-1) re m_ncr[i][j];
    re m_ncr[i][j]=ncr(i-1,j) + ncr(i-1,j-1);
}*/

/*ll m_fact[21];
ll fact(ll i)
{
    if(i==1) re 1;
    if(m_fact[i]!=-1) re m_fact[i];
    re m_fact[i]=i*func(i-1);
}*/

ll flg,ch[11],cas;

void check(ll n)
{
    while(n)
    {
        if(ch[n%10]==0)
        {
            flg++;
            ch[n%10]=1;
        }
        n/=10;
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    freopen("A-large.in", "r", stdin);
    freopen("a.out", "w", stdout);
    ll int t,i,j,x,n,cnt=0,m,y,nn;
    cin>>t;
    while(t--)
    {
        cin>>n;
        memo(ch,0);
        nn=0;
        if(n==0)
        {
            cout<<"Case #"<<++cas<<": INSOMNIA"<<endl;
            continue;
        }
        cnt=flg=0;
        while(flg<10)
        {
            nn+=n;
            check(nn);
        }
        cout<<"Case #"<<++cas<<": "<<nn<<endl;
    }
}
