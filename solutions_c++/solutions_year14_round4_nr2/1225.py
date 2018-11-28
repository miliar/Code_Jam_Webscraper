#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <algorithm>
using namespace std;

int a[1111];
int main(){
    int data[10];
    int cc, tt;
    scanf("%d", &tt);
    for (int cc = 1; cc <= tt; cc++){
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
            scanf("%d", &a[i]);
        for (int i = 0; i < n; i++)
            data[i] = i;
        int best_ans = -1;
        do{
            int count = 0;
            int mode = 0;
            for (int i = 0; i < n-1; i++){
                if (mode == 0 && a[data[i]] < a[data[i + 1]])
                    continue;
                if (mode == 0)
                    mode = 1;
                if (mode == 1 && a[data[i]] > a[data[i + 1]])
                    continue;
                mode = -1;
            }
            if (mode != -1){
                for (int i = 0; i < n;i++)
                for (int j = i+1; j < n; j++){
                    if (data[i]>data[j])
                        count++;
                }
                if (best_ans == -1 || best_ans>count)
                    best_ans = count;
            }
        } while (next_permutation(data, data + n));
        printf("Case #%d: %d\n", cc, best_ans);
    }
    return 0;
}