#include <bits/stdc++.h>

using namespace std;

int main()
{
    int tc;
    cin >> tc;
    for (int T = 0; T < tc; T++) {
        string s;
        cin >> s;
        vector<int> cnt(26, 0);
        for (int i = 0; i < (int)s.size(); i++) {
            cnt[s[i]-'A']++;
        }
        vector<int> num_cnt(10, 0);
        cout << "Case #" << T+1 << ": ";

        // Z W U G
        // 0 2 4 8
        char ch1[4] = {'Z', 'W', 'U', 'G'};
        int n1[4] = {0, 2, 4, 8};
        string s1[4] = {"ZERO", "TWO", "FOUR", "EIGHT"};
        for (int i = 0; i < 4; i++) {
            int c = cnt[ch1[i]-'A'];
            if (c > 0) {
                num_cnt[n1[i]] = c;
                for (int j = 0; j < (int)s1[i].size(); j++) {
                    cnt[s1[i][j]-'A'] -= c;
                }
            }
        }           

        // ONE THREE FIVE SIX SEVEN NINE
        // O T F X
        // 1 3 5 6
        char ch2[4] = {'O', 'T', 'F', 'X'};
        int n2[4] = {1, 3, 5, 6};
        string s2[4] = {"ONE", "THREE", "FIVE", "SIX"};
        for (int i = 0; i < 4; i++) {
            int c = cnt[ch2[i]-'A'];
            if (c > 0) {
                num_cnt[n2[i]] = c;
                for (int j = 0; j < (int)s2[i].size(); j++) {
                    cnt[s2[i][j]-'A'] -= c;
                }
            }
        }
        
        // SEVEN NINE
        // S I
        // 7 9
        char ch3[2] = {'S', 'I'};
        int n3[4] = {7, 9};
        string s3[4] = {"SEVEN", "NINE"};
        for (int i = 0; i < 2; i++) {
            int c = cnt[ch3[i]-'A'];
            if (c > 0) {
                num_cnt[n3[i]] = c;
                for (int j = 0; j < (int)s3[i].size(); j++) {
                    cnt[s3[i][j]-'A'] -= c;
                }
            }
        }

        for (int i = 0; i < 10; i++) {
            while (num_cnt[i] > 0) {
                num_cnt[i]--;
                cout << i;
            }
        }
        cout << endl;
    }

    return 0;
}
