#include <bits/stdc++.h>
using namespace std;
struct _ { ios_base::Init i; _() { cin.sync_with_stdio(0); cin.tie(0);cout.tie(0); } } _;
#define READ(FILE) freopen(FILE,"r",stdin)
#define WRITE(FILE) freopen(FILE,"w",stdout)
#define ict int t;cin>>t;while(t--)
#define lct long long int t;cin>>t;while(t--)
#define in(a) int a; cin>>a;
#define llin(a) ll a; cin>>a;
#define srep(i,a,b) for(ll i=a;i<b;i++)
#define rep(i,n) for(ll i=0;i<n;i++)
#define pb push_back
typedef long long int ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef pair<ll,ll> pll;
typedef set<int> si;
typedef set<ll> sl;
typedef map<string, ll> mapsl;
typedef map<string, int> mapsi;
typedef map<int,int> mapii;
typedef map<ll, ll> mapll;


int main()
{
    freopen("inputFiles/A-large.in","r",stdin);
    freopen("inputFiles/ans.txt","w",stdout);
    in(T);
    for(int t=1;t<=T;t++)
    {
        string str; cin>>str;
        in(K);
        int times=0;
        bool possible=true;
        for(int i=0;i<str.length() && possible;i++)
        {
            if(str[i]=='-')
            {
                times++;
                int j=i;
                if(i+K-1>=str.length())
                    possible=false;

                while(j<=i+K-1 && possible)
                {
                    if(str[j]=='+')
                        str[j]='-';
                    else
                        str[j]='+';
                    j++;

                }
            }
        }

        if(!possible)
        cout<<"Case #"<<t<<": "<<"IMPOSSIBLE"<<endl;
        else
        cout<<"Case #"<<t<<": "<<times<<endl;
    }

}
