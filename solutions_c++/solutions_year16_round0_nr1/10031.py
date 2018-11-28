#include <iostream>
#include <cstdio>
#include <set>
#include <string>

using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int T;
    scanf("%d", &T);

    for(int i=0; i<T; i++) {
        int n;
        scanf("%d", &n);

        set<long long> table1,table2;

        for(long long j=1;;j++) {
            long long tn = n*j;
            if(table2.find(tn) != table2.end()) {
                printf("Case #%d: INSOMNIA\n", i+1);
                break;
            }
            table2.insert(tn);
            do {
                table1.insert(tn % 10);
                tn /= 10;
            } while (tn != 0);

            if (table1.size() == 10) {
                printf("Case #%d: %lld\n", i+1, j*n);
                break;
            }
        }
    }
    return 0;
}