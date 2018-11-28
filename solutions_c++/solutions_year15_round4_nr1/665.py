#include <stdio.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <set>
#include <algorithm>
#include <map>
#include <vector>
#include <deque>

using namespace std;

int N, M, K, T;
int R, C;
char input[128][128];
int input_num[128][128];

int run()
{
    int res = 0;
    memset(input_num, 0, sizeof(input_num));
    scanf("%d%d", &R, &C);
    for(int i = 0; i < R; ++i) {
        scanf("%s", input[i]);
    }

    for(int i = 0; i < R; ++i) {
        for(int j = 0; j < C; ++j) {
            if(input[i][j] == '.') {
                continue;
            }
            if(input[i][j] == '<') {
                ++res;
            }
            input_num[i][j]++;
            break;
        }
        for(int j = C - 1; j >= 0; --j) {
            if(input[i][j] == '.') {
                continue;
            }
            if(input[i][j] == '>') {
                ++res;
            }
            input_num[i][j]++;
            break;
        }
    }
    for(int j = 0; j < C; ++j) {
        for(int i = 0; i < R; ++i) {
            if(input[i][j] == '.') {
                continue;
            }
            if(input[i][j] == '^') {
                ++res;
            }
            input_num[i][j]++;
            break;
        }
        for(int i = R - 1; i >= 0; --i) {
            if(input[i][j] == '.') {
                continue;
            }
            if(input[i][j] == 'v') {
                ++res;
            }
            input_num[i][j]++;
            if(input_num[i][j] >= 4) {
                printf("IMPOSSIBLE\n");
                return 0;
            }
            break;
        }
    }
    printf("%d\n", res);
    return 0;
}

int main()
{
    scanf("%d", &T);
    for(int i = 0; i < T; ++i) {
        printf("Case #%d: ", i + 1);
        run();
    }
    return 0;
}


