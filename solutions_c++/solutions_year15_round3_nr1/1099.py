#include <bits/stdc++.h>
using namespace std;

#define READ(in)      freopen(in,"r",stdin)
#define WRITE(out)    freopen(out,"w",stdout)

#define FOR(i, s, e)  for(int i=s; i<=e; i++)
#define FOREACH(i,n)  for(__typeof(n.begin()) i=n.begin();i!=n.end();i++)
#define SCI(x) scanf("%d", &x)
#define SCII(x, y) scanf("%d %d", &x, &y)
#define SCIII(x, y, z) scanf("%d %d %d", &x, &y, &z)

#define SET(x, y) memset(x, y, sizeof(x))

#define pb            push_back
#define mp            make_pair
#define ff            first
#define ss            second

#define DB(x)         cerr << #x << " = " << x << endl;

#define MAX (long long unsigned) (1e18) + 7
#define mod 1000000007

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int main(){
    //ios_base::sync_with_stdio(false);
    READ("in.txt");
    WRITE("out.txt");
    int t, kase=1, r, c, w, x;
    cin >> t;
    while(t--){
        cin >> r >> c >> w;
        x = c/w;
        printf("Case #%d: ", kase++);
        cout << r*x+w-1 + (c%w>0) << endl;
    }


    return 0;
}
