#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

int main() {
    
    int n;
    cin >> n;
    
    vector<string> answers;
    
    for (int i = 1; i <= n; ++i){
        string s;
        cin >> s;
        string ans = "";
        for (int j = 0; j < s.length(); ++j){
            if (ans.size() == 0){
                ans += s[j];
            }
            else if (s[j] >= ans[0]){
                ans = s[j] + ans;
            }
            else{
                ans += s[j];
            }
        }
        
        answers.push_back(ans);
    }
    
    for (int i = 0; i < n; ++i){
        cout << "Case #" << i + 1 << ": " << answers[i] << endl;
    }
    
    return 0;
}
