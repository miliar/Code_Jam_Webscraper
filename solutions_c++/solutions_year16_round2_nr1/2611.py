#include<iostream>
#include<string>
#include<vector>

using namespace std;

class Solution {
public :
    void reduce(vector<int>& num, string s, int i){
        for (auto c : s) {
            num[c-'A'] -= i;
        }
    }
    string getDigits(string& s){
        vector<int> num(26, 0);
        vector<int> cnt(10, 0);
        for (auto i : s) {
            num[i-'A']++;
        }
        cnt[0] += num['Z'-'A'];
        reduce(num, "ZERO", num['Z'-'A']);
        cnt[2] += num['W'-'A'];
        reduce(num, "TWO", num['W'-'A']);
        cnt[6] += num['X'-'A'];
        reduce(num, "SIX", num['X'-'A']);
        cnt[8] += num['G'-'A'];
        reduce(num, "EIGHT", num['G'-'A']);
        
        cnt[3] += num['T'-'A'];
        reduce(num, "THREE", num['T'-'A']);
        cnt[7] += num['S'-'A'];
        reduce(num, "SEVEN", num['S'-'A']);
        cnt[5] += num['V'-'A'];
        reduce(num, "FIVE", num['V'-'A']);
        cnt[4] += num['F'-'A'];
        reduce(num, "FOUR", num['F'-'A']);
        cnt[1] += num['O'-'A'];
        reduce(num, "ONE", num['O'-'A']);
        cnt[9] += num['I'-'A'];
        reduce(num, "NINE", num['I'-'A']);
        string ans;
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < cnt[i]; j++) {
                ans += to_string(i);
            }
        }
        return ans;
    }
    
};
int main(){
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        string s;
        cin >> s;
        Solution solution;
        cout << "Case #" << i << ": " << solution.getDigits(s) << endl;
    }
    return 0;
}
