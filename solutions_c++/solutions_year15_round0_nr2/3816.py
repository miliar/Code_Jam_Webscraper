#include <bits/stdc++.h>

using namespace std;

int input[1005];

int solve(int index) {
    if (index == 0) return 0;
    if (input[index] == 0) {
        return solve(index-1);
    }
    int mini = index;
    int value = input[index];
    input[index] = 0;
    for (int i = 1; i <= index/2; ++i) {
        //cout << "go into index: " << index-1 << endl;
        //cout << input[i] << " " << input[index-i] << endl;
        input[i] += value;
        input[index-i] += value;
        //cout << input[i] << " " << input[index-i] << endl;
        mini = min(mini, value + solve(index-1));
        //cout << input[i] << " " << input[index-i] << endl;
        input[i] -= value;
        input[index-i] -= value;
        //cout << "go out of index: " << index-1 << endl;
        //cout << input[i] << " " << input[index-i] << endl;
    }
    input[index] = value;
    return mini;
}

int main () {
    int tcase;
    scanf("%d", &tcase);
    for (int j = 1; j <= tcase; ++j) {
        memset(input, 0, sizeof(input));

        int num;
        scanf("%d", &num);
        int maxi = 0;
        for (int i = 0; i < num; ++i) {
            int target;
            scanf("%d", &target);
            maxi = max(maxi, target);
            ++input[target];
        }
        printf("Case #%d: %d\n", j, solve(maxi));
    }
    return 0;
}
