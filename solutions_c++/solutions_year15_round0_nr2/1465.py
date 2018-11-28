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

#define MOD(x) x%10000007
#define MAX (long long unsigned) (1e18) + 7

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int main()
{
    READ("in.txt");
    WRITE("out.txt");
    ios_base::sync_with_stdio(false);

    int t, d, x, kase=1;
    int ara[1005];
    cin >> t;
    while(t--){
        SET(ara, 0);

        cin >> d;
        FOR(i, 1, d){
            cin >> x;
            for(int j=1; j<x; j++){
                ara[j] += ceil(x/(j*1.0)) - 1;
            }
        }

        int mn=1005;
        FOR(i, 1, 1001){
            mn = min(mn, ara[i]+i);
            //cout << i << " " << ara[i] << endl;
        }
        printf("Case #%d: %d\n", kase++, mn);
    }

    fclose(stdin);
    fclose (stdout);
    return 0;
}
