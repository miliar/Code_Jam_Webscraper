#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <bitset>
#include <sstream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <functional>
#include <iomanip>
#include <cstdlib>

const int mx = 1010;
using namespace std;

int n, t, x, v[mx], ans;

int main(){
//    freopen("data.in","r",stdin);
//    freopen("data.out","w",stdout);
    scanf("%d", &t);
    for(int j = 1 ; j <= t ; j++){
        scanf("%d", &n);
        for(int i = 0; i < n ; i++){
            scanf("%d", &v[i]);
        }
        sort( v, v + n);
        ans = v[ n - 1 ];
        for(int i = 1 ; i <= v[ n - 1 ] ; i++){
            int k = i;
            for(int j = 0 ; j < n ; j++){
                if(i < v[j]){
                    k += (v[j] / i - (int)(v[j] % i == 0));
                }
            }
            ans = min(ans, k);
        }
        printf("Case #%d: %d\n", j, ans);
    }
    return 0;
}

