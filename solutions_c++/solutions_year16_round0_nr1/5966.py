#include <iostream>
#include <cstdio>
#include <unordered_map>
#include <vector>
#include <map>

using namespace std;

const int N = 1000001;
unordered_map<int, int> ans;

void init() {
    for(int i = 1; i < N; ++ i) {
        int t = 1;
        unordered_map<int, bool> umap;
        while(1) {
            int tmp = i * t;
            while(tmp) {
                umap[tmp % 10] = true;
                tmp /= 10;
            }
            bool flag = false;
            for(int j = 0; j < 10; ++ j) {
                if(!umap[j]) {
                    flag = true;
                    break;
                }
            }
            if(!flag) {
                ans[i] = i*t;
                break;
            }
            t ++;
        }
    }
}

int main()
{
    init();

    int num, tcase;
    freopen("A-large.in", "r", stdin);
    freopen("A-large.txt", "w", stdout);
    scanf("%d", &tcase);

    for(int i = 1; i <= tcase; ++ i) {
        scanf("%d", &num);
        printf("Case #%d: ", i);
        if(num == 0) {
            printf("INSOMNIA\n");
        }
        else {
            printf("%d\n", ans[num]);
        }
    }
    fclose(stdout);
    fclose(stdin);

    return 0;
}
