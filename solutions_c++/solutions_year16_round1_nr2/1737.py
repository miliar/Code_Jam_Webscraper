#include<cstdio>
#include<map>

using namespace std;

int t, casei, n;

int main() {
    casei = 0;
    scanf("%d", &t);
    while(t--) {
        scanf("%d", &n);
        int tmp;
        map<int, int> m;
        for(int i = 0; i < 2 * n - 1; ++i) {
            for(int j = 0; j < n; j++) {
                scanf("%d", &tmp);
                ++m[tmp];
            }
        }
        printf("Case #%d:", ++casei);
        for(auto x : m) {
            if(x.second % 2) printf(" %d", x.first);
        }
        printf("\n");
    }
    return 0;
}
