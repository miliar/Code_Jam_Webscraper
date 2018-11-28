#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <algorithm>
using namespace std;

int w[11111];
int sent[111111];
int main(){

    int cc, tt;
    scanf("%d", &tt);
    for (int cc = 1; cc <= tt; cc++){
        int n, x, ans = 0;
        scanf("%d%d", &n, &x);
        for (int i = 0; i < n; i++){
            scanf("%d", &w[i]);
        }
        sort(w, w + n);
        memset(sent, 0, sizeof(sent));

        for (int i = 0; i < n; i++){
            if (sent[i])
                continue;
            sent[i] = 1;
            ans++;
            for (int j = n - 1; j >= 0; j--){
                if (sent[j] || w[i] + w[j]>x)
                    continue;
                sent[j] = 1;
                break;
            }
        }
        printf("Case #%d: %d\n", cc, ans);
    }
    return 0;
}