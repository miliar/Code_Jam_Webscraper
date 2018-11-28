#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string.h>
#include <iostream>

using namespace std;

void solve() {
    char search_c[] = {'Z', 'O', 'W', 'T', 'U', 'V', 'X', 'S', 'G', 'I'};
    int arr[] = {0, 2, 4, 6, 8, 1, 7, 5, 9, 3};
    string words[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
    int words_len[] = {4, 3, 3, 5, 4, 4, 3, 5, 5, 4};
    string s;
    cin >> s;
    vector<int> count(26);
    int l = s.length();
    for(int i = 0; i < l; i++) {
        count[s[i]-'A']++;
    }
    vector <int> counter(10);
    for(int i = 0; i <= 9; i++) {
        int a = arr[i];
        int b = words_len[a];
        counter[a] = count[search_c[a]-'A'];
        for(int j = 0; j < b; j++) {
            count[words[a][j]-'A'] = count[words[a][j]-'A'] - counter[a];
        }
    }
    for(int i = 0; i < 10; i++) {
        int a = counter[i];
        for(int j = 0; j < a; j++) {
            printf("%d", i);
        }
    }
    printf("\n");
}

int main() {
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++) {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
