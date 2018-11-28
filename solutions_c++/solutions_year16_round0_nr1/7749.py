
#include <bits/stdc++.h>

using namespace std;



#define ll long long
#define ull long long int
#define pll pair<LL, LL>
#define pii pair<int,int>

#define mp make_pair
#define pb push_back
#define fs first
#define sc second

#define INF_MAX 3000000000
#define INF_MIN -2147483647
#define EPS 1e-6
#define MOD (1000000007)
#define PI  2*acos(0);

#define fore(iter,v) for(iter=v.begin(); iter!=v.end(); iter++)
#define forup(i,a,n) for(i=a; i<n; i++)
#define rep(i,n) for(i=0; i<n; i++)
#define SET(a, v) memset(a, v, sizeof a)
#define all(a) a.begin(),a.end()
#define ALLOC0(N)   (int*)calloc(N, sizeof(int));

#define gi(x) scanf("%d",&x)
#define gl(x) scanf("%lld",&x)


#define ps(x) printf("%s",x)
#define pi(x) printf("%d",x)
#define pl(x) printf("%lld", x)
#define pn printf("\n")
#define spc printf(" ")
#define prec(x) cout<<fixed<<setprecision(x)

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ios_base::sync_with_stdio(false);
    ll t,bk;
    cin>>t;
    for(bk=1;bk<=t;bk++)
    {
        cout<<"Case #"<<bk<<": ";
        ll n,a[10]={0},k=1,temp=0,temp1,temp2,c=0;
        cin>>n;
        if(n==0)
        {
            cout<<"INSOMNIA"<<endl;
            continue;
        }
        while(c!=10)
        {
            temp+=n;
            temp2=temp;
            while(temp2>0)
            {
                temp1=temp2%10;
                temp2/=10;
                if(a[temp1]==0)
                {
                    a[temp1]=1;
                    c++;
                }
            }
        }
        cout<<temp<<endl;
    }
}
