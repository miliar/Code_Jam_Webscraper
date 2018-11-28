#include <bits/stdc++.h>
using namespace std;

string words[] = {"zero", "two", "six", "four", "five", "eight", "three", "seven", "one", "nine"};
int vlrs[] = {0, 2, 6, 4, 5, 8, 3, 7, 1, 9};
char let[] = {'z', 'w', 'x', 'u', 'f',  'g', 'h', 's', 'o', 'n'};

int main(){
    int t, cases = 1;
    cin >> t;
    while (t--){
        string s;
        cin >> s;

        vector<int> ch(27, 0);
        for (int i = 0; i < s.length(); i++){
            ch[s[i]-'A']++;
        }

        vector<int> ans;

        for (int i = 0; i < 10; i++){
            int l = INT_MAX;
            for (int j = 0; j < words[i].length(); j++){
                l = min(l, ch[words[i][j]-'a']);
            }
            for (int j = 0; j < words[i].length(); j++){
                ch[words[i][j]-'a'] -= l;
            }
            for (int j = 0; j < l; j++)
                ans.push_back(vlrs[i]);
        }

        sort(ans.begin(), ans.end());

        cout << "Case #" << cases++ << ": ";
        for (int i = 0; i < ans.size(); i++)
            cout << ans[i];
        cout << endl;
    }
    return 0;
}
