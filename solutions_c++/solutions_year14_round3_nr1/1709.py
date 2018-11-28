#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <string>
#include <functional>
#include <utility>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

void print_vector(vi v);
void print_array(int* array, int start, int end);

#define FOR(i,a,b) for (int i = (a),_b = (b); i < _b; i++)
#define DOW(i,b,a) for (int i = (b),_a = (a); i > _a; i--)
#define fill(a,v) memset(a, v, sizeof a)
#define checkbit(n,b) ((n >> b) & 1)
#define pb(a) push_back(a)
#define ALL(a) (a).begin(), (a).end()
#define SZ(a) (int)(a).size()

#define INF 1e9
#define PI acos(-1.0)

#define s(n)                        scanf("%d",&n)
#define sc(n)                       scanf("%c",&n)
#define sl(n)                       scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
#define ss(n)                       scanf("%s",n)

int tc, cse = 1;
char line[100];

ll a, b;

ll gcd(ll a, ll b){
    return a == 0 ? b : gcd(b % a, a);
}

bool isPowerOfTwo(ll a){
    FOR(i, 0, 50){
        if((1 << i) & a){
            return (a - (1 << i)) == 0;
        } else {
            continue;
        }
    }
    return false;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    s(tc);
    getchar();
    while(tc--){
        scanf("%lld/%lld", &a, &b);
       
        ll g = gcd(a, b);
        a /= g;
        b /= g;
        bool sol = true;
        int times = 0;
        if(!isPowerOfTwo(b)){
            sol = false;
        } else {
            while(b != 1){
                if(a <= b/2){
                   // printf("%lld %lld\n", a, b);
                    b /= 2;
                    times++;
                } else {
                    times++;
                    break;
                }
            }
        }
        if(!sol){
            printf("Case #%d: impossible\n", cse++);
        } else {
            printf("Case #%d: %d\n", cse++, times);
        }
        
    }
    return 0;
}

void print_array(int* array, int start, int end){
  printf("[");
  FOR(i, start, end){
    printf("%d ", array[i]);
  }
  printf("]");
  printf("\n");
}

void print_vector(vi v){
  printf("[");
  FOR(i, 0, v.size()){
    printf("%d ", v[i]);
  }
  printf("]");
  printf("\n");
}