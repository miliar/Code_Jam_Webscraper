#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <cctype>
#include <cstring>
#include <vector>
#include <sstream>
#include <set>
#include <ctime>
#include <queue>
#include <map>
#include <cmath>
using namespace std;
int n , s , a[10000] , cas = 0;
int main(){
    // freopen("A-large.in" , "r" , stdin);
    // freopen("A.out" , "w" , stdout);
    int t;
    cin >> t;
    while (t --) {
        cin >> n >> s;
        for (int i = 0 ; i < n ; ++i) 
            cin >> a[i];
        sort(a , a + n);
        int ans = 0;
        int head = 0;
        for (int i = n - 1 ; i >= head ; --i){
            ++ans;
            if (a[i] + a[head] <= s) ++head;
        }
        printf("Case #%d: %d\n" , ++cas , ans);
    }
    return 0;
}
