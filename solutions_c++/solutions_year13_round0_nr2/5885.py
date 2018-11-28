#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <cstring>

#define N 100

using namespace std;

int arr[N][N], arr2[N][N], a = 2, b = 1;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    scanf("%d", &t);
    for(int p = 0; p < t; p++) {
        printf("Case #%d: ", p + 1);

        int n, m;
        scanf("%d %d", &n, &m);

        int c = 0;
        for(int i = 0; i < n; i++)
            for(int j = 0; j < m; j++) {
                scanf("%d", &arr[i][j]);
                if(arr[i][j] == b)  c++;
            }

        for(int i = 0; i < n; i++)
            for(int j = 0; j < m; j++)  arr2[i][j] = a;
        bool flag;
        for(int i = 0; i < n; i++) {
            flag = true;
            int k = 0;
            for(int j = 0; j < m; j++) {
                if(arr[i][j] > b) {
                    flag = false;
                    break;
                }
            }
            if(flag) {
                for(int j = 0; j < m; j++) {
                    if(arr2[i][j] == a) k++;
                    arr2[i][j] = b;
                }
                c -= k;
            }
        }
        for(int i = 0; i < m; i++) {
            int k = 0;
            flag = true;
            for(int j = 0; j < n; j++) {
                if(arr[j][i] > b) {
                    flag = false;
                    break;
                }
            }
            if(flag) {
                for(int j = 0; j < n; j++) {
                    if(arr2[j][i] == a) k++;
                    arr2[j][i] = b;
                }
                c -= k;
            }
        }

        if(c == 0)  puts("YES");
        else    puts("NO");

        /*for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++)  printf("%d ", arr2[i][j]);
            putchar('\n');
        }*/
    }
}
