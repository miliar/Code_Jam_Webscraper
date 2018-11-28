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
    int t, n, x, kase=1;
    string str;
    cin >> t;
    while(t--){
        cin >> n >> str;
        int cnt = 0, req = 0;
        for(int i=0; i<str.size(); i++){
            x = str[i] - '0';
            if(i>cnt){
                req += i-cnt;
                cnt = i+x;
            }
            else{
                cnt += x;
            }
        }
        //DB(cnt);
        printf("Case #%d: %d\n", kase++, req);
    }

    fclose(stdin);
    fclose (stdout);
    return 0;
}
