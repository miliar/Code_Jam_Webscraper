#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
using namespace std;
//#define Max        100000
#define xx         first
#define yy         second
#define pb         push_back
#define mp         make_pair
#define ll         long long
//#define inf        INT_Max/3
#define mod        1000000007ll
#define PI         acos(-1.0)
#define linf       (1ll<<60)-1
#define FOR(I,A,B) for(int I = (A); I < (B); ++I)
#define REP(I,N)   FOR(I,0,N)
#define ALL(A)     ((A).begin(), (A).end())
#define set0(ar)   memset(ar,0,sizeof ar)
#define vsort(v)   sort(v.begin(),v.end())
#define setinf(ar) memset(ar,126,sizeof ar)
#define MaxC 100000
#define N 20
#define Max 100000 // Why? :D
#define inf 10007
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("A-large.in","r", stdin);
    freopen("output.out","w", stdout);
    #endif


    int i,j,k,l,m,n,o,p,kase=1;

    cin>>n;
    while(kase<=n){
        string s;
        cin>>m>>s;
        //cout<<s<<endl;
        int cumsum=0;
        int tottal=0;
        for(int i=0;i<s.length();i++){
            //cout<<"CUMSUM: "<<cumsum<<endl;
            if(i>cumsum&&s[i]>'0'){
                //cout<<"cumsum: "<<cumsum<<endl;
                int tt=i-cumsum;
                tottal=tottal+tt;
                //cout<<"Tottal "<<tottal<<endl;
                cumsum=cumsum+tt;
                cumsum=cumsum+(s[i]-'0');

            }
            else{
               cumsum=cumsum+(s[i]-'0');

            }
        }
        cout<<"Case #"<<kase++<<": "<<tottal<<endl;
    }
    return 0;


}
