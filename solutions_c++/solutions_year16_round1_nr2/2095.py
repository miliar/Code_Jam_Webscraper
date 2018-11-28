/* @coder: Sidharth Gupta */

#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string>
#include <cassert>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>


#define MOD 109546051211ll
#define MIN(a,b) ((a)>(b)?(b):(a))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define ABS(a) MAX(a,-(a))
#define SET(a,b) memset(a, b, sizeof(a))
#define EVEN(a) ((a&1)==0)
#define SQR(a) ((a)*(a))
#define EPS 0.0001

typedef long long int lli;
typedef unsigned long long int llui;
typedef unsigned int uint;

using namespace std;

int main() {

    int T, t, n, num;
    int arr[2505];

    scanf("%d", &T);

    for(t=1; t<=T; ++t) {

        scanf("%d", &n);
        SET(arr, 0);

        for(int i=0; i< n*(2*n-1); ++i) {
            scanf("%d", &num);
            ++arr[num];
        }

        printf("Case #%d:", t);
        for(int i=1;i<=2500;++i) {
            if(!EVEN(arr[i])) {
                printf(" %d", i);
            }
        }
        if(t!=T) printf("\n");
    }

    return 0;
}
