#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std ;

int a[1111] , f[1111] ;
//int dfs(int now) {
//    if(now <= 2) return 2 ;
//    int ans = 0 ;
//    if(now % 2) {
//        ans += dfs(now / 2 + 1) + dfs(now / 2) ;
//    }
//    else ans += dfs(now / 2) + dfs(now / 2) ;
//    return ans ;
//}
#include <set>
#include <vector>vv ;
//struct cmp{
//    int x ;
//    bool operator < (const cmp & fk) const {
//        return x > fk.x ;
//    }
//} ;
bool cmp(const int &x , const int &y) {
    return x > y ;
}
void dfs(int *a ,)
int main() {
    int t ;
//    for (int i = 0 ; i < 1111 ; i ++ ) f[i] = i ;
//    f[1] = 1 , f[2] = 2 , f[3] = 3 ;
//    for (int i = 4 ; i < 1011 ; i ++ ) {
//        for (int j = 1 ; j < i ; j ++ ) {
//            f[i] = min(f[i] , max(f[j] , f[i - j]) + 1) ;
//        }
//    }
//    for (int i = 0 ; i < 11 ; i ++ ) cout << f[i] << ":" ;
//    freopen("B-small-attempt5.in","r",stdin) ;
//    freopen("B-small-attempt5.out","w",stdout) ;
    cin >> t ;int ca = 0 ;

//    cout << f[4] << endl;
    while(t -- ) {
        int x ;
//        vector<cmp> vv ;
//        set<int ,cmp > c ;
//        c.clear() ;
        cin >> x ;
        int sum = 0 ;
        for (int i = 0 ; i < x ; i ++ ) {
            scanf("%d" , a + i ) ;
//            sum = max(sum , a[i]) ;
//            vv.push_back(a[i]) ;
//            c.insert(a[i]) ;
        }
//        ans = sum ;
        sort(a , a + x , cmp) ;
        int split = 0 ;
        int ans = a[0] ;
        while(a[0] != 1) {
            ans = min(ans , a[0] + split) ;
            int v = a[0] ;
            if(v & 1) {
                a[0] = v / 2 ;
                a[x ++ ] = v / 2 + 1 ;
            }
            else {
                a[0] = v / 2 ;
                a[x ++ ] = v / 2 ;
            }
            split ++ ;
            sort(a , a + x , cmp) ;
            cout << a[0] + split << "   :    " ;
            for (int i = 0 ; i < x ; i ++ ) cout << a[i] << " " ;cout << endl;
        }
//        for (set<int> :: iterator it = c.begin() ;it != c.end() ;++ it) cout << *it << endl;
//        if(x == 1) sum = f[a[0]] ;
        printf("Case #%d: %d\n", ++ ca , ans) ;
    }
    return 0 ;
}
