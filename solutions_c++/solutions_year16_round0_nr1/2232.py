#include <iostream>
#include <cstdio>
#include <set>
using namespace std;
bool check(set<int> &s, int n) {
    while (n > 0) {
        s.insert(n%10);
        n /= 10;
    }
    return s.size() == 10;
}
int main() {
    int t;
    scanf("%d",&t);
    for (int tc=1; tc<=t; tc++) {
        int n;
        scanf("%d",&n);
        printf("Case #%d: ",tc);
        if (n == 0) {
            printf("INSOMNIA\n");
        } else {
            set<int> s;
            for (int i=1;; i++) {
                bool ok = check(s, n*i);
                if (ok) {
                    printf("%d\n",n*i);
                    break;
                }
            }
        }
    }
    return 0;
}
