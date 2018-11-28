#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef map<int,int> mii;
typedef vector<int> vi;
typedef vector<pii> vpii;
typedef vector< vector<int> > vvi;
typedef vector< vector<pii> > vvpii;

#define rep(i,n) for(int i=0;i<int(n);i++)
#define forup(i,a,b) for(int i=int(a);i<=int(b);i++)
#define fordn(i,a,b) for(int i=int(a);i>=int(b);i--)
#define fi first
#define se second
#define all(x) x.begin(),x.end()
#define permute(x) next_permutation(all(x))
#define mp make_pair
#define pb push_back
#define INF 2000000000 // 2 * 10^9
#define MOD 1000000007 // 10^9 + 7
#define debug if(printf("JJ "))
#define trace(x) cout << #x << " = " << x << endl
#define trace2(x,y) cout << #x << " = " << x << " " << #y << " = " << y << endl 

int main(){
    int t,n,extra,ppl;
    char s[1005];    
    scanf("%d",&t);
    forup(zz,1,t){
        ppl = extra = 0;
        scanf("%d %s",&n,s);n++;
        rep(i,n){
            if((s[i]-'0') > 0){
                if(ppl < i) extra+=(i-ppl), ppl=i;
                ppl += (s[i]-'0');
            }
        }
        printf("Case #%d: %d\n",zz,extra);
    }
}
