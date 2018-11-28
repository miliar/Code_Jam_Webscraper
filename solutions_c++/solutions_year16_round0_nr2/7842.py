
#include <bits/stdc++.h>

using namespace std;



#define ll long long
#define ull unsigned long long
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
        string s;
        ll i,k=0,c=0,n;
        cin>>s;
        n=s.size();
        for(i=0;i<n;i++)
        {
            while(i!=s.size() && s[i]==s[k])
                i++;
            k=i;
            i--;
            c++;
        }
        if(s[n-1]=='+')
            c--;
        cout<<c<<endl;
    }
}
