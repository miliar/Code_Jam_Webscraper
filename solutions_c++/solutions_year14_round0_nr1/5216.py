#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <sstream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <map>
#include <set>


using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
#define ill long long
#define sz(a) int((a).size())
#define pb push_back
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define inf 100000000
#define si(x) scanf("%d", &(x));
#define pi(x) printf("%d\n", (x));
#define sill(x) scanf("%lld", &(x));
#define pill(x) printf("%lld\n", (x));


vector <vector<int> > v1, v2;

int main()
{
    int t, cs = 1, r1, r2, cnt, ans;
    freopen ("A-small-attempt0.in", "r", stdin);
    freopen ("output.txt", "w", stdout);
    si(t);

    while (cs <= t) {
        v1.clear();
        v2.clear();

        v1.resize(4, vector<int>(4) );
        v2.resize(4, vector<int>(4) );
        cnt = 0;

        si(r1);
        r1--;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                si(v1[i][j] );

        si(r2);
        r2--;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                si(v2[i][j] );

        for (int j = 0; j < 4; j++) {
            int x = v1[r1][j];
            for (int k = 0; k < 4; k++) {
                if (v2[r2][k] == x) { ans = x; cnt++; }
            }
        }

        if (cnt == 1) cout << "Case #" << cs << ": " << ans << endl;
        if (cnt > 1) cout << "Case #" << cs << ": Bad magician!" << endl;
        if (cnt == 0) cout << "Case #" << cs << ": Volunteer cheated!" << endl;
        cs++;
    }
    return 0;
}




