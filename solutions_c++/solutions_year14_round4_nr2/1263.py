#include <fstream>
#include <algorithm>
#include <cmath>

using namespace std;

const int MAXN = 1005;
int a[MAXN], perm[MAXN], n;

bool check() {
    int i = 1;
    while(i < n && a[perm[i]] > a[perm[i - 1]])
        i++;
    for(; i < n; i++)
        if(a[perm[i]] > a[perm[i - 1]])
            return false;
    return true;
}

int get() {
    int res = 0;
    for(int i = 0; i < n; i++)
        for(int j = i + 1; j < n; j++)
            if(perm[i] > perm[j])
                res++;
    return res;
}

int main() {
    ifstream in("input.txt");
    ofstream out("output.txt");
    int t;
    in >> t;
    for(int tt = 0; tt < t; tt++) {
        in >> n;
        for(int i = 0; i < n; i++)
            in >> a[i];
        for(int i = 0; i < n; i++)
            perm[i] = i;
        int f = 1;
        for(int i = 1; i <= n; i++)
            f *= i;
        int ans = n * n;
        for(int i = 0; i < f; i++) {
            if(check())
                ans = min(ans, get());
            next_permutation(perm, perm + n);
        }
        out << "Case #" << tt + 1 << ": " << ans << '\n';
    }
    return 0;
}
