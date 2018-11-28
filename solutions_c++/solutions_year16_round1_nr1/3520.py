#include<iostream>
#include<string>
using namespace std;

class Solution {
public :
    string getLastWord(string& s){
        string res;
        res += s[0];
        for (int i = 1; i < s.size(); i++) {
            if (s[i] >= res[0]) {
                res = s[i] + res;
            }else{
                res += s[i];
            }
        }
        return res;
    }
    
};
int main(){
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        string s;
        cin >> s;
        Solution solution;
        cout << "Case #" << i << ": " << solution.getLastWord(s) << endl;
    }
    return 0;
}
