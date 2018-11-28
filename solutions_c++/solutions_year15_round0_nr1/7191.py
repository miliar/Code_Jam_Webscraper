#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define sz size()
#define ln length()
#define rep(i,n)  for(int i=0;i<n;i++)
#define fu(i,a,n) for(int i=a;i<=n;i++)
#define fd(i,n,a) for(int i=n;i>=a;i--)
#define all(a)    a.begin(),a.end()
#define si(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define gl(n) cin >> n
#define pi(n) printf("%d",n)
#define pl(n) cout << n
#define ps printf(" ")
#define pn printf("\n")
#define MAX 1000007

int main()
{
    //freopen("A-small-attempt0.in","rt",stdin);
    //freopen("A-small.out","wt",stdout);
    freopen("A-large.in","rt",stdin);
    freopen("A-large.out","wt",stdout);

    int T;
    si(T);
    rep(t,T)
    {
        int N;
        string S;
        si(N);
        cin>>S;
        int A[S.sz+2];
        int tot[S.sz+2];
        memset(tot,0,sizeof tot);
        tot[0]=S[0]-'0';
        rep(i,S.sz)
        {
            A[i] = S[i]-'0';
            if(i>0)
            tot[i]=tot[i-1]+A[i];
        }
        int ans=tot[S.sz-1],cnt=0;
        for(int i=1;i<S.sz;i++)
        {
            //cout<<i<<" "<<A[i]<<" "<<tot[i-1]<<endl;
            if(A[i]==0)
                continue;
            if(A[i] != 0 && tot[i-1] >= i)
                continue;
            else
            {
                cnt+=(i-tot[i-1]);
                for(int j=i;j<S.sz;j++)
                    tot[j]+=(i-tot[i-1]);
            }
        }
        cout<<"Case #"<<t+1<<": "<<cnt<<endl;
    }
    return 0;
}

