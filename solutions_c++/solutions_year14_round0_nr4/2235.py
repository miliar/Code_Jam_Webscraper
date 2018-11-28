#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <map>
#include <sstream>
#include <set>
#include <vector>
#include <string>
#include <queue>
#define INF 1000000000
#define eps 1e-8
#define lld long long
#define mem(a,b) memset((a),(b),sizeof((a)))
using namespace std;

int a[2000], b[2000];
int n, i, j;
set<int> s;
int main() {
    int T,cas=0;
        freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    cin>>T;

    while(T--) {
        scanf("%d", &n);
        for(i = 0; i < n; i++) {
            double x;
            scanf("%lf", &x);
            a[i] = (int)floor(1000000 * x);
        }
        for(i = 0; i < n; i++) {
            double x;
            scanf("%lf", &x);
            b[i] = (int)floor(1000000 * x);
        }
        sort(a, a + n);
        sort(b, b + n);
        int ans1 = 0, ans2 = 0;
        s.clear();
        for(i = 0; i < n; i++)
            s.insert(b[i]);
        for(i = n - 1; i >= 0; i--){
            set<int>::iterator it;
            it = s.lower_bound(a[i]);
            if (it == s.end()){
                it--;
                s.erase(it);
                ans1++;
            } else if (it != s.begin()){
                it--;
                s.erase(it);
                ans1++;
            } else if (it == s.begin()){
                s.erase(it);
            }
        }
        s.clear();
        for(i = 0; i < n; i++)
            s.insert(b[i]);
        for(i = n - 1; i >= 0; i--){
            set<int>::iterator it;
            it = s.lower_bound(a[i]);
            if (it == s.end()){
                ans2++;
                it = s.begin();
                s.erase(it);
            } else{
                s.erase(it);
            }
        }
        printf("Case #%d: %d %d\n", ++cas, ans1, ans2);
    } fclose(stdin);
    fclose(stdout);
    return 0;
}
