#include<cstdio>
#include<vector>
using namespace std;

struct party {
    char number;
    int count;
};

int main() {
    int tc_count;
    scanf("%d", &tc_count);
    ++tc_count;
    auto cmp = [](const party& a, const party& b) { return a.count > b.count; };
    for (int tc = 1; tc < tc_count; ++tc) {
        int n;
        scanf("%d", &n);
        vector<party> p(n);
        for (int i = 0; i < n; ++i) {
            p[i].number = 'A' + i;
            scanf("%d", &p[i].count);
        }

        sort(begin(p), end(p), cmp);

        printf("Case #%d:", tc);

        while (p[0].count - p[1].count > 1) {
            printf(" %c%c", p[0].number, p[0].number);
            p[0].count -= 2;
        }
        if (p[0].count > p[1].count) {
            printf(" %c", p[0].number);
            --p[0].count;
        }

        for (int i = n - 1; i > 1; --i) {
            while(p[i].count > 1) {
                printf(" %c%c", p[i].number, p[i].number);
                p[i].count -= 2;
            }
            if (p[i].count > 0) {
                printf(" %c", p[i].number);
                --p[i].count;
            }
        }

        while (p[0].count > 0) {
                printf(" %c%c", p[0].number, p[1].number);
                --p[0].count;
        }

        printf("\n");
    }
    return 0;
}
