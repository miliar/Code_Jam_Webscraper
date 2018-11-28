#include <bits/stdc++.h>

using namespace std;

int main(){
    int t;
    string s;
    char best;
    cin >> t;
    for (int l = 0; l < t; l++){
        cin >> s;
        best = s[0];
        stack<char> b;
        queue<char> e;
        for (int i = 0; i < s.size(); i++){
            if (s[i] >= best){
                best = s[i];
                b.push(s[i]);
            }
            else
                e.push(s[i]);
        }
        cout << "Case #" << l+1 << ": ";
        while (!b.empty()){
            cout << b.top();
            b.pop();
        }
        while (!e.empty()){
            cout << e.front();
            e.pop();
        }
        cout << "\n";
    }
    return 0;
}
