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

int cas;

int main()
{
    ios_base::sync_with_stdio(0);
    freopen("B-large.in", "r", stdin);
    freopen("b.out", "w", stdout);
    int i,j,x,n,cnt=0,m,y,t;
    cin>>t;
    string in;
    vector<int>v;
    while(t--)
    {
        cin>>in;
        if(in[0]=='-')
            v.pb(0);
        else
            v.pb(1);
        n=sz(in)-1;
        fr(i,1,n)
        {
            if(in[i]!=in[i-1])
            {
                if(in[i]=='-')
                    v.pb(0);
                else
                    v.pb(1);
            }
        }
        n=sz(v)-1;
        x=v[n];
        m=cnt=0;
        while(sz(v)>1)
        {
            //cout<<sz(v)<<" "<<v[0]<<" "<<m<<" "<<cnt<<endl;
            if(sz(v)>3)
            {
                if(m%2)
                    v[0]=!v[0];
                if(v[0]==x)
                {
                    cnt+=3;
                    y=4;
                }
                else
                {
                    cnt+=2;
                    y=3;
                }
                cnt++;
                v.erase(v.begin(),v.begin()+y);
                if(sz(v)>1)
                    reverse(v.begin(),v.end()-1);
                //else if(y==4)
                    //cnt--;
                m++;
            }
            else if(sz(v)==3)
            {
                if(m%2)
                    v[0]=!v[0];
                cnt+=2;
                break;
            }
            else
            {
                cnt++;
                break;
            }
        }
        if(x==0)
            cnt++;
        cout<<"Case #"<<++cas<<": "<<cnt<<endl;
        v.clear();
    }
}
