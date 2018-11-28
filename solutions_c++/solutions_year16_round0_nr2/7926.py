#include <iostream>
#include <string>

using namespace std;
using ull = unsigned long long;

int main(){
    
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t){
        cout << "Case #" << t << ": ";
        string s;
        cin >> s;
        char c[2] = {'+', '-'};
        int cnt = 0;
        for(int i = s.size() - 1; i >= 0; --i){
            if(c[cnt & 1] != s[i]){
                ++cnt;
            }
        }
        cout << cnt << endl;
    }
    return 0;
}