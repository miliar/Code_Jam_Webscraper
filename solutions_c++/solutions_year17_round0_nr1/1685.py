#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
#define mod(a,b) ((a)%(b)+(b))%(b)
#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(auto i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define rep(i,n) for(int (i)=0;(i)<int((n));(i)++)


void solve(){
    char S[1005];
    int K,C=0;
    scanf("%s %d", S, &K);
    vi A(strlen(S));
    rep(i,sz(A))
        A[i]=S[i]=='+'?1:0;
    rep(i,sz(A)-K+1)
        if(!A[i]){
            rep(j,K)
                A[i+j]=1-A[i+j];
            C++;
        }
    bool P=true;
    rep(i,K-1)
        if(!A[sz(A)-i-1]){
            P=false;
            break;
        }
    if(P)
        printf("%d\n",C);
    else
        printf("%s\n","IMPOSSIBLE");
}
int main() {
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int T;
    scanf("%d",&T);
    //cin.ignore(numeric_limits<streamsize>::max(), '\n');
    rep(n,T) {
        fprintf(stderr,"%d\n",n+1);
        printf("Case #%d: ",n+1);
        solve();
    }
}
