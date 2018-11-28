#include<iostream>
#include<string>
using namespace std;

class Solution {
public :
    long long int getTimes(string s){
        long long int res = 0;
        for (int i = s.size()-1; i >= 0; i--) {
            if (s[i] == '-') {
                res++;
                for (int j = i-1; j >= 0; j--) {
                    if (s[j] == '+') {
                        s[j] = '-';
                    }else{
                        s[j] = '+';
                    }
                }
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
        cout << "Case #" << i << ": " << solution.getTimes(s) << endl;
    }
    return 0;
}
