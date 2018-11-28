#include <iostream>
#include <climits>
#include <algorithm>
#include <string>

using namespace std;

void solve(){
    string s;
    cin >> s;

    string answer;
    answer += s[0];
    for(int i = 1; i < s.size(); i++){
        if(answer[0] <= s[i]){
            answer.insert(0, 1, s[i]);
        } else {
            answer.push_back(s[i]);
        }
    }
    cout << answer << endl;

}

int main(){
    int T;
    cin >> T;
    for(int i = 0; i < T; i++){
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
}
