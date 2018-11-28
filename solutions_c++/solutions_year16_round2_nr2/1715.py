#include <bits/stdc++.h>

using namespace std;
int cases = 1;

string nums[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

bool can(int av[], string num) {
    for (int j = 0; j < num.size(); ++j) {
        av[num[j] - 'A']--;
        if (av[num[j] - 'A'] < 0)return 0;
    }
    return 1;
}

bool done(int av[]) {
    for (int i = 0; i < 27; ++i) {
        if (av[i] != 0)return 0;
    }
    return 1;
}

string best(string out, int av[]) {
    if (done(av))return out;
    for (int i = 0; i < 10; ++i) {
        int BB[27];
        for (int k = 0; k < 27; ++k) {
            BB[k] = av[k];
        }
        if (can(BB, nums[i])) {
            for (int j = 0; j < nums[i].size(); ++j) {
                av[nums[i][j] - 'A']--;
            }
            int B[27];
            for (int k = 0; k < 27; ++k) {
                B[k] = av[k];
            }
            string ret = best(out + to_string(i), B);
            if (!ret.empty())return ret;
            for (int j = 0; j < nums[i].size(); ++j) {
                av[nums[i][j] - 'A']++;
            }
        }
    }
    return "";
}

int main(void) {
    freopen("/home/vanessi/ClionProjects/CodeJamR1BA/in.in", "r", stdin);
    freopen("/home/vanessi/ClionProjects/CodeJamR1BA/out.out", "w", stdout);
    for (int j = 0; j < 10; ++j) {
        sort(nums[j].begin(), nums[j].end());
    }
    int t;
    scanf("%d", &t);
    while (t--) {
        string in;
        cin >> in;
        int arr[27];
        for (int j = 0; j < 27; ++j) {
            arr[j] = 0;
        }
        for (int i = 0; i < in.size(); ++i) {
            arr[in[i] - 'A']++;
        }
        printf("Case #%d: ", cases++);
        cout << best("", arr) << "\n";
    }
}