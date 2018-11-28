#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>
#define MAXS 11
using namespace std;

int count_flips(vector<int> &binary) {
    int count = 0;
    int last = binary[0];

    for (int i = 0; i < binary.size(); i++) {
        if(binary[i] == last) continue;

        count++;
        last = binary[i];
    }

    if(last == 0) count++;

    return count;
}

int get_ans(string value) {
    vector<int> binary;

    for(int i = 0; i < value.size(); i++) {
        if(value[i] == '-')
            binary.push_back(0);
        else binary.push_back(1);
    }

    return count_flips(binary);
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int t;
    vector<int> ans;
    string value;

    scanf("%d", &t);

    for(int i = 1; i <= t; i++) {
        cin >> value;
        ans.push_back(get_ans(value));
    }

    for(int i = 0; i < ans.size(); i++)
        printf("Case #%d: %d\n", i+1, ans[i]);
    return 0;
}
