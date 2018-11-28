#include <bits/stdc++.h>
using namespace std;
const int N = 105;
int ca;

int n , m , f[N] , deg[N];
char a[N];
char str[5][50];
int cnt[5];
bool v[N];
vector<int> e[N];
void work() {
    cerr << ca << endl;
    scanf("%d" , &n);
    for (int i = 1 ; i <= n ; ++ i) {
        e[i].clear();
    }
    for (int i = 1 ; i <= n ; ++ i) {
        int x;
        scanf("%d" , &x);
        f[i] = x;
        if (x) {
            e[x].push_back(i);
        }
    }
    scanf("%s" , a + 1);
    scanf("%d" , &m);
    for (int i = 0 ; i < m ; ++ i) {
        scanf("%s" , str[i]);
    }
    memset(cnt , 0 , sizeof(cnt));


    srand(time(0));
    int TT = 100000;
    vector<int> V;
    for (int t = 0 ; t < TT ; ++ t) {
        for (int i = 1 ; i <= n ; ++ i) {
            V.push_back(i);
            v[i] = 0;
        }

        static char s[N];
        for (int i = 0 ; i < n ; ++ i) {
            int x = V[rand() % V.size()];
            while (f[x] && !v[f[x]]) {
                x = f[x];
            }
            v[x] = 1;
            s[i] = a[x];
            for (int j = 0 ; j < V.size() ; ++ j) {
                if (V[j] == x) {
                    swap(V[j] , V.back());
                    V.pop_back();
                    break;
                }
            }
        }
        s[n] = 0;
        for (int i = 0 ; i < m ; ++ i) {
            if (strstr(s , str[i])) {
                ++ cnt[i];
            }
        }
    }
    for (int i = 0 ; i < m ; ++ i) {
        printf("%.10f%c" , 1.0 * cnt[i] / TT , " \n"[i + 1 == m]);
    }


}

int main() {
    freopen("in" , "r" , stdin);
    freopen("out2" , "w" , stdout);
    int T;
    scanf("%d" , &T);
    while (T --) {
        printf("Case #%d: " , ++ ca);
        work();
    }
    return 0;
}
