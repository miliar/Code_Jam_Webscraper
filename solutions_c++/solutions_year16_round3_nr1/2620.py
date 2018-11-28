
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


struct com
{
    char c;
    ll val;
};



bool fun(com a,com b)
{
    return a.val>b.val;
}

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
        ll n,temp,i,sum=0;
        com temp1;

        vector<com> v;
        cin>>n;
        for(i=0;i<n;i++)
        {
            cin>>temp;
            temp1.c=i+'A';
            temp1.val=temp;
            v.push_back(temp1);
            sum+=temp;
        }
        while(true)
        {
            sort(v.begin(),v.end(),fun);
            if(v.size()==2 && v[0].val==v[1].val)
            {
                for(i=0;i<v[0].val;i++)
                    cout<<v[0].c<<v[1].c<<" ";
                break;
            }
            else
            {
                v[0].val--;
                cout<<v[0].c<<" ";
            }

            if(v[0].val==0)
                v.erase(v.begin());
        }
        cout<<endl;
    }
}
