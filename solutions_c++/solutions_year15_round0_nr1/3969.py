/**
                                                ooooooo
                                                o         ooooooo   ooooooo   o ooooo  ooooooo
                                                ooooooo    oooooo    oooooo    o    o  o
                                                      o    o    o    o    o    o    o  o
                                                ooooooo    ooooooo   ooooooo   o    o  ooooooo
*/

#include<bits/stdc++.h>
using namespace std;
#define loop(i,n) for(i=0;i<n;i++)
#define loop1(i,n) for(i=1;i<=n;i++)
#define loop3(i,n,k) for(i=n;i<=k;i++)
#define loopr(i,n,k) for(i=n;i>=k;i--)
#define pvn(n) cout<<n<<"\n"
#define pvw(n) cout<<n<<" "
#define pvpn(n,x) cout<< std::fixed;cout<< std::setprecision(x)<<n<<"\n"
#define pvpw(n,x) cout<< std::fixed;cout<< std::setprecision(x)<<n<<" "
#define pw cout<<" "
#define pn cout<<"\n"
#define TZ(n) __builtin_ctz(n)
#define LZ(n) __builtin_clz(n)
#define CSB(n) __builtin_popcount(n)

#define MAX 1000000007
#define pi  3.1415926535
#define exp  2.7182818284

typedef long long int LL;
typedef long int L;
typedef double D;
typedef unsigned long long int ULL;
typedef vector<LL> VLL;
typedef vector<L> VL;
typedef vector<int> VI;
typedef vector<char> VC;
typedef vector<string> VS;
typedef vector<float> VF;
typedef vector<double> VD;
typedef pair<LL,LL> PLL;

const LL INF=1000000000;

int main()
{
    std::ios::sync_with_stdio(false);
    LL i,j,t,k=0,l,n,x,y,ans;
    string s;
    cin>>t;
    while(t--)
    {
        k++;
        LL ans=0;
        cin>>n>>s;
        x=0;
        loop(i,n+1)
        {
            if(x<i){
                ans+=(i-x);
                x=i;
            }
            x+=(s[i]-48);
        }
        cout<<"Case #"<<k<<": "<<ans<<endl;
    }
    return 0;
}
