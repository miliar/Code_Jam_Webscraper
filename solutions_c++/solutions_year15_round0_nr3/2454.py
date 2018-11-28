#include <bits/stdc++.h>
using namespace std;

int trans[5][5] = { {0, 1, 2, 3, 4},
                    {0, 1, 2, 3, 4},
                    {0, 2, -1, 4, -3},
                    {0, 3, -4, -1, 2},
                    {0, 4, 3, -2, -1} };

int pattern, repeat;
char input[10005];

inline void deal(int id, int start, bool* negtive, int* value, int*cut_point, const int& mysize) {
    for (int i = start; i < mysize; ++i) {
        if (value[id] != id+2 || negtive[id]) {
            value[id] = trans[value[id]][input[i]-'i'+2];
            if (value[id] < 0) {
                negtive[id] = !negtive[id];
                value[id] = -value[id];
            }
            continue;
        }
        else {
            cut_point[id] = i;
            return;
        }
    }
}

inline void cal_last(int start, bool* negtive, int*value, int* cut_point, const int& mysize) {
    for (int i = cut_point[1]; i < mysize; ++i) {
        value[2] = trans[value[2]][input[i]-'i'+2];
        if (value[2] < 0) {
            negtive[2] = !negtive[2];
            value[2] = -value[2];
        }
    }
}

bool solve() {
    if (pattern*repeat < 3) return false;
    int mysize = pattern*repeat;
    int value[] = {0, 0, 0};
    bool negtive[] = {false, false, false};
    int cut_point[] = {-1, -1};

    deal(0, 0, negtive, value, cut_point, mysize);
    if (cut_point[0] < 0) return false;
    deal(1, cut_point[0], negtive, value, cut_point, mysize);
    if (cut_point[1] < 0) return false;
    cal_last(cut_point[1], negtive, value, cut_point, mysize);
    if (value[2] == 4 && !negtive[2]) return true;

    bool new_try = true;
    for (int i = cut_point[0]; i < mysize; ++i) {
        if (new_try) {
            new_try = false;
            value[0] = trans[value[0]][input[i]-'i'+2];
            if (value[0] < 0) {
                negtive[0] = !negtive[0];
                value[0] = -value[0];
            }
            continue;
        }
        if (value[0] == 2 && !negtive[0]) {
            value[1] = 0; negtive[1] = false;
            deal(1, cut_point[0], negtive, value, cut_point, mysize);
            if (cut_point[1] < 0) return false;
            value[2] = 0; negtive[2] = false;
            cal_last(cut_point[1], negtive, value, cut_point, mysize);
            if (value[2] == 4 && !negtive[2]) return true;
            else new_try = true;
        }
        else {
            value[0] = trans[value[0]][input[i]-'i'+2];
            if (value[0] < 0) {
                negtive[0] = !negtive[0];
                value[0] = -value[0];
            }
        }
    }

    return false;
}

int main () {
    int tcase;
    scanf("%d", &tcase);
    for (int j = 1; j <= tcase; ++j) {
        scanf("%d%d", &pattern, &repeat);
        scanf("%s", input);
        for (int i = 0; i < pattern; ++i) {
            for (int k = 1; k < repeat; ++k) {
                input[i+pattern*k] = input[i];
            }
        }
        if (solve()) {
            printf("Case #%d: YES\n", j);
        }
        else {
            printf("Case #%d: NO\n", j);
        }
    }
    return 0;
}
