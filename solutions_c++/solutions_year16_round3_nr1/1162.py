#include <iostream>
#include <stdio.h>
#include <fstream>
#include <queue>
#include <iomanip>
#include <cstdio>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <time.h>
#include <cassert>
#include <map>
#include <set>
#include <stack>
#include <time.h>
#include <cstdlib>
#include <cstring>
#include <string.h>
#include <bitset>

#include <complex>

//#include <unordered_map>
//#include <unordered_set>

#define llong long long int
#define pb push_back
#define mp make_pair
#define pr pair <int, int>
#define X first
#define Y second
#define endl "\n"
using namespace std;
const int MAXN = 5e5 + 7;
//const int INF = 1e9 + 7;
//const llong LINF = 1e18;
const llong MOD = 1e9 + 7;
//const long double EPS = 1e-18;
using namespace std;
int tests;
int a[30];
int main() {
#ifdef DEBUG
    
    double beg = clock();
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
#else
    //freopen("centroid.in", "r", stdin);
    //freopen("centroid.out", "w", stdout);
#endif
    //ios_base::sync_with_stdio(0);cin.tie();
    scanf("%d", &tests);
    for (int test = 1; test <= tests; test++) {
        int n;
        scanf("%d", &n);
        
        for (int i = 1; i <= n; i++) {
            a[i] = 0;
        }
        int mn = 1000;
        set <pr, greater<pr>> S;
        for (int i = 1; i <= n; i++) {
            scanf("%d", &a[i]);
            mn = min(mn, a[i]);
            S.insert(mp(a[i], i));
        }
        string ans;
        while (!S.empty()) {
            if (S.begin()->first == mn) {
                break;
            }
            
                ans += char('A' + S.begin()->second - 1);
                ans += " ";
            pr tmp = *S.begin();
            S.erase(S.begin());
            tmp.first--;
            a[tmp.second]--;
            S.insert(tmp);
        }
        pr who =  {-1, -1};
        for (int i = 1; i <= n; i++) {
            if (a[i] > 0) {
                if (who.first == -1) {
                    who.first = i;
                } else if (who.second == -1) {
                    who.second = i;
                } else {
                    while (a[i]) {
                        ans += char('A' + i - 1);
                        ans += " ";
                        a[i]--;
                    }
                }
            }
        }
        while (a[who.first] > 0) {
            ans += char(who.first + 'A' - 1);
            ans += char(who.second + 'A' - 1);
            ans += " ";
            a[who.first]--;
        }
        printf("Case #%d: %s\n", test, ans.c_str());
        
        
        
        
    }
#ifdef DEBUG
    double end = clock();
    fprintf(stderr, "\n*** Total time = %.3lf ***\n", (end - beg) / CLOCKS_PER_SEC);
#endif
    return 0;
}