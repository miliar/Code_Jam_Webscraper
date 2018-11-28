#include <cstdio>
#include <cstring>
#define MAX 110

int n, size;
char panc[MAX];
bool cont[MAX];

int main() {
    scanf("%d", &n);
    for (int cas = 1; cas <= n; cas++) {
        int ans = 0;
        bool even;
        scanf("%s", panc);
        size = strlen(panc);
        for (int i = 0; i < size; i++)
            cont[i] = panc[i] == '+';
        even = cont[0];
        for (int i = 0; i < size; i++)
            if (!cont[i]) {
                for (int j = i; j < size && !cont[j]; j++)
                    cont[j] = true;
                ans++;
            }
        printf("Case #%d: %d\n", cas, ans * 2 - !even);
    }
    return 0;
}
