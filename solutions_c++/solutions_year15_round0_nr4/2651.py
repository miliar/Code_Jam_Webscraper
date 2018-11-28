#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <sstream>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <limits>
#include <iomanip>

#define INF 1000000000
#define Inf 1000000000000000000
#define mp make_pair
#define pb push_back
#define EPS 1e-9

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vii> vvii;

int main() {
    //freopen("in","r",stdin);
    //freopen("out","w",stdout);
    int t,x,r,c;
    cin >> t;
    for(int cas = 1; cas <= t; ++cas)
    {
        cin >> x >> r >> c;
        if (r > c) swap(r,c);
        bool richard = false;
        switch (x) {
            case 1:
                break;
            case 2:
                if ((r == 1 && c == 1) || (r == 1 && c == 3) || (r == 3 && c == 3))
                    richard = true;
                break;
            case 3:
                if ((r == 1) || (r == 2 && c == 2) || (r == 2 && c == 4) || (r == 4 && c == 4))
                    richard = true;
                break;
            case 4:
                if ((r == 3 && c == 4) || (r == 4 && c == 4))
                    richard = false;
                else
                    richard = true;
                break;
            default:
                break;
        }
        if (richard) printf("Case #%d: RICHARD\n",cas);
        else printf("Case #%d: GABRIEL\n",cas);
    }
    return 0;
}
