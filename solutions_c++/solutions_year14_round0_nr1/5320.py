#include <vector>
#include <string>
#include <cstring>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <ctime>
using namespace std;
#define FOR(i,a,b) for(int i=a; i<=b; i++)
#define REP(i,a,b) for(int i=a; i>=b; i--)
#define FORAD(i,u) for(int i=0; i < (int)u.size(),i++)
#define BUG(x) cout << x << endl
#define ll long long
#define fi first
#define sd second
#define pb push_back
#define two(i) 1 << i
#define sz(x) (int)x.size()
#define e 1e-12
#define bit(s,i) ((s >> (i-1)) & 1)
#define Nmax 100100
const double pi = acos(-1);
typedef vector<int> vi ;
typedef pair<int,int> pii ;

int dd[20], row, test, dem;

int main() {
    freopen("in.inp","r",stdin);
    freopen("ans.out","w",stdout);
    scanf("%d", &test);
    FOR(t, 1, test){
        FOR(i, 1, 16) dd[i] = 0;
        FOR(k, 1, 2){
            scanf("%d", &row);
            FOR(i, 1, 4) FOR(j, 1, 4) {
                int x;
                scanf("%d", &x);
                if (i == row) dd[x]++;
            }
        }
        dem = 0;
        FOR(i, 1, 16) if (dd[i] == 2) dem++;
        printf("Case #%d: ", t);
        if (dem == 1) {FOR(i, 1, 16) if (dd[i] == 2) printf("%d\n", i);}
        else if (dem > 1) printf("Bad magician!\n"); else printf("Volunteer cheated!\n");
    }
     return 0;
}
