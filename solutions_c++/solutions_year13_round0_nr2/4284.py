#include <cstring>
#include <cstdlib>
#include <climits>
#include <cstdio>
#include <cctype>
#include <cmath>

#include <iostream>
#include <algorithm>
#include <utility>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>

using namespace std;
#define fr(i,j,k) for (int (i) = (j); (i) < (k); (i)++)
#define frd(i,j,k) for (int (i) = (j); (i) >= (k); (i)--)
#define ms(ar,a) memset(ar, a, sizeof(ar))
#define db(x) cerr << #x << " == " << x << endl
#define _ << ", " <<
#define ler(a) scanf("%d", &a)
#define ler2(a,b) scanf("%d%d", &a, &b)
#define pb push_back
#define mp make_pair
#define INF 0x3f3f3f3f
typedef long double ld;
typedef long long ll;
typedef pair<int, int> pii;
const double PI = acos(-1.0);
template <class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }
#define MAXN 100

int grid[101][101];

bool testcoll(int x, int pos, int limite){
    for(int i = 0;i<limite;i++){
        if(x<grid[i][pos]){
            return false;
        }
    }
    return true;
}
bool testrow(int x, int pos, int limite){
    for(int i = 0;i<limite;i++){
        if(x<grid[pos][i]){
            return false;
        }
    }
    return true;
}

int main(){

	freopen("a.txt","r",stdin);
	freopen("b.txt","w",stdout);
    int t, caso = 1, n, m, x;
    ler(t);
    while(t--){
        ler2(n,m);
        for(int i = 0;i<n;i++){
            for(int j=0;j<m;j++){
                ler(grid[i][j]);
            }
        }
        bool resp = true;
        for(int i = 0;i<n && resp;i++){
            for(int j=0;j<m && resp;j++){
                resp = (resp && (testcoll(grid[i][j],j,n) || testrow(grid[i][j],i,m) ) );
            }
        }
        if(resp){
            printf("Case #%d: YES\n",caso++);
        }else{
            printf("Case #%d: NO\n",caso++);
        }
    }
	return 0;
}
