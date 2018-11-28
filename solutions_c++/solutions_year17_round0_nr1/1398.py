///==================================================///
///                HELLO WORLD !!                    ///
///                  IT'S ME                         ///
///               BISHAL GAUTAM                      ///
///         [ bsal.gautam16@gmail.com ]              ///
///==================================================///
#include<bits/stdc++.h>
#define X first
#define Y second
#define mpp make_pair
#define nl printf("\n")
#define SZ(x) (int)(x.size())
#define pb(x) push_back(x)
#define pii pair<int,int>
#define pll pair<ll,ll>
///---------------------
#define S(a) scanf("%d",&a)
#define P(a) printf("%d",a)
#define SL(a) scanf("%lld",&a)
#define S2(a,b) scanf("%d%d",&a,&b)
#define SL2(a,b) scanf("%lld%lld",&a,&b)
///------------------------------------
#define all(v) v.begin(),v.end()
#define CLR(a) memset(a,0,sizeof(a))
#define SET(a) memset(a,-1,sizeof(a))
#define fr(i,a,n) for(int i=a;i<=n;i++)
using namespace std;
typedef long long ll;

///  Digit     0123456789012345678 ///
#define MX     2005
#define inf    2000000010
#define MD     1000000007
#define eps    1e-9
///===============================///

char s[MX+2];
int n,k;

int FindLatestMinus(int id){
    for(int i=id;i<n;i++){
        if( s[i]=='-') return i;
    }
    return -1;
}

int main() {
    freopen("A-large.in","r",stdin);
    freopen("OutputLargeA.txt","w",stdout);
    int tc,cs=1,i,j;
    S(tc);
    while(tc--) {
       scanf("%s %d",s,&k);
       n=strlen(s);
       int cnt=0;
       bool f=1;
       int pid=0;
       //cout<< " N: "<<n<<endl;
       while( true ){
           int id=FindLatestMinus(pid);
          // cout<< "Id: "<<id<<endl;
           if( id==-1 )break;
           if( id+k>n ){
               f=0;
               break;
           }
           for(i=id;i<id+k;i++){
               if( s[i]=='+' )s[i]='-';
               else s[i]='+';
           }
           pid=id;
           cnt++;
       }
       if(!f) {
            printf("Case #%d: IMPOSSIBLE\n",cs++);
       }
       else{
         printf("Case #%d: %d\n",cs++,cnt);
       }
    }
    return 0;
}
