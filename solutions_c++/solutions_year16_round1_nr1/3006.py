#include <iostream>

using namespace std;

int main(){
    string ch;
    int tc;
    cin >> tc;
    string ans;
    for(int c = 1; c <= tc; c++){
        ans = "";
        cin >> ch;
        for(int i = 0; i < ch.size(); i++){
            if(ch[i] >= ans[0]) ans.insert(ans.begin(), ch[i]);
            else ans.push_back(ch[i]);
        }
        cout << "Case #" << c << ": " << ans << '\n';
    }
    return 0;
}
