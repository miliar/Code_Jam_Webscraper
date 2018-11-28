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

    int t, x, r, c, kase=1;
    cin >> t;
    while(t--){
        cin >> x >> r >> c;
        if(r<c) swap(r, c);
        bool richard = false;
        //DB(r);
        //DB(c);

        richard |= (r*c)%x;
        richard |= x>r && x>c; ///line

        int tr= x/2, tc= x/2;
        if(x%2==0) tr++;
        else tr++, tc++;
        richard |= (tr > r) || (tc > c); ///2-3 case
        richard |= (c>1) && (x-c+1 > c); ///z case
        richard |= x>=7;

        if(richard) printf("Case #%d: RICHARD\n", kase++);
        else printf("Case #%d: GABRIEL\n", kase++);


    }

    fclose(stdin);
    fclose (stdout);
    return 0;
}
