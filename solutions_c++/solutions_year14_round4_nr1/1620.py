#include <cstdio>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <ctime>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <deque>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <bitset>

#define FOR(i, a, b) for (i = (a); i <= (b); i++)
#define REP(i, a) for (i = 0; i < (a); i++)
#define ALL(v) (v).begin(), (v).end()
#define SET(a, x) memset((a), (x), sizeof(a))
#define SZ(a) ((int)(a).size())
#define CL(a) ((a).clear())
#define SORT(x) sort(ALL(x))
#define mp make_pair
#define pb push_back
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))

#define filer() freopen("in.txt","r",stdin)
#define filew() freopen("out.txt","w",stdout)

using namespace std;

typedef long long ll;
typedef unsigned long long llu;

int arr[10005], ks;
int N, X;

int main(){
    int test;
    
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    while ( scanf("%d", &test) == 1 ){
        for ( ks = 1 ; ks <= test ; ks++ ){
            cin >> N >> X;
            
            for ( int i= 0 ; i < N ; i++ ) cin >> arr[i];
            sort(arr, arr + N);
            
            int cnt = 0;
            int i, j;
            for ( i = 0, j = N - 1 ; i < j ; i++, j-- ){
                if ( arr[i] + arr[j] <= X ) cnt++;
                else{
                    cnt++;
                    i--;
                }
                
                //printf("%d %d\n", i, j);
            }
            
            if ( i == j ) cnt++;
            printf("Case #%d: %d\n", ks , cnt);
        }
    }
    
    return 0;
}
