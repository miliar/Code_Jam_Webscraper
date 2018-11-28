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


bool palim(long long x){
    char cc[10];
    int pos = 0;
    int r;
    while(x > 0){
        r = x%10;
        x = x/10;
        cc[pos++] = '0'+r;
    }
    for(int i = 0;i<pos;i++){
        if(cc[i] != cc[pos-1-i]){
            return false;
        }
    }
    return true;
}

int main(){

	freopen("a.txt","r",stdin);
	freopen("b.txt","w",stdout);
    int t, caso = 1;
    ler(t);
    long long maior, menor;
    while(t--){
        scanf("%lld%lld",&menor,&maior);
        long long r1 = (long long)sqrt(maior);
        int cont = 0;
        while(r1>0){
            if(r1*r1 < menor){
                break;
            }
            if(palim(r1)){
                if(palim(r1*r1)){
                    cont++;
                }
            }
            r1--;
        }
        printf("Case #%d: %d\n",caso++,cont);
    }
	return 0;
}
