#include<bits/stdc++.h>

using namespace std;

#define read(fn) freopen(fn,"r",stdin)
#define write(fn) freopen(fn,"w",stdout)
#define pi acos(-1.0)
#define clr(a) memset(a,0,sizeof(a))
#define set(a) memset(a,-1,sizeof(a))
#define pb push_back
#define sz(a) ((int)a.size())
#define all(a) a.begin(),a.end()
#define foreach(i, c) for( __typeof( (c).begin() ) i = (c).begin(); i != (c).end(); ++i )
#define ff first
#define ss second
#define mp make_pair
#define inf (1<<30)
#define eps 1e-9
#define iseq(a,b) (fabs(a-b)<eps)
#define sc(a) scanf("%c", &a)
#define ss(a) scanf("%s", a)
#define sd(a) scanf("%d", &a)
#define slld(a) scanf("%lld", &a)
#define dbg(x) cout<<#x<<" : "<<x<<endl
#define mod 1000000007LL
typedef long long int lld;

#define mx 1009


int main(){
    //read("A-large.in");
    //write("ALargeOut.txt");
    int T;
    sd(T);
    for(int line=1; line<=T; line++){
        char in[mx];
        int sm;
        sd(sm);
        scanf("%s", in);
        int res = 0, total = 0;
        for(int i=0; i<=sm; i++){
            if(i <= total) total += in[i] - '0';
            else{
                res += i - total;
                total = i + in[i] - '0';
            }
        }
        printf("Case #%d: %d\n", line, res);
    }
    return 0;
}
