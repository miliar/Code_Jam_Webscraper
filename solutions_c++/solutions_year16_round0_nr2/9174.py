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
#define INF 100000000000000
#define pi  3.1415926535
#define exp  2.7182818284

#define MP(x,y) make_pair(x,y)

typedef long long int LL;
typedef long int L;
typedef long double LD;
typedef unsigned long long int ULL;
typedef vector<LL> VLL;
typedef vector<L> VL;
typedef vector<int> VI;
typedef vector<char> VC;
typedef vector<string> VS;
typedef vector<float> VF;
typedef vector<double> VD;
typedef pair<LL,LL> PLL;



int main(){
    std::ios::sync_with_stdio(false);
    LL t,n,m,i,j,x=0;
    cin>>t;
    while(t--){
        x++;
        cout<<"Case #"<<x<<": ";
        string s;
        cin>>s;
        LL ans=0;
        i=0;
        if(s[0]=='-')
            ans++;
        while(i<s.size() && s[i]=='-'){
            i++;
        }
        while(i<s.size()){
            if(s[i]=='+')i++;
            else{
                ans+=2;
                while(i<s.size() && s[i]=='-')
                    i++;
            }
        }
        pvn(ans);
    }
    return 0;
}
