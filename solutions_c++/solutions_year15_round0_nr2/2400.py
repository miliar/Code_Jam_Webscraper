#include <algorithm>
#include <numeric>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <complex>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef set<int> se;
typedef pair<int,int> pii;
typedef long long int tint;

#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define decl(v, c) typeof(c) v = c
#define forall(i, c) for(decl(i, c.begin()); i!=c.end(); ++i)
#define rall(c) (c).rbegin(), (c).rend()
#define all(c) (c).begin(), (c).end()
#define D(a) << #a << "=" << a << " "


#define si(a) int((a).size())
#define pb push_back
#define mp make_pair

const int MAXN = 1000 + 10;
int P[MAXN];

int main () {
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);

	ios_base::sync_with_stdio(false);

	int T;

	cin >> T;

	forsn(caso,1,T+1) {

        int D; cin >> D;
        forn(i,D) cin >> P[i];

        int res = 1e6;

        forsn(eat, 1, MAXN) {
            int count = eat;
            forn(i,D) {
                if (P[i] <= eat) continue;
                count += (P[i] + eat - 1) / eat - 1;
            }
            res = min(res,count);
        }


        cout << "Case #" << caso << ": "<< res << endl;
	}

  return 0;

}


