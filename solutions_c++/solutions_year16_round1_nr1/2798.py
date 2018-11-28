#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL),cout.tie(NULL);
    deque<char> s;
    int t;
    cin >> t;
    string str;
    for(int cn = 1;cn<=t;cn++){
        cin >> str;
        s.clear();
        s.push_back(str[0]);
        for(int i=1;i<str.size();i++){
            if (str[i] >= s.front()){
                s.push_front(str[i]);
            }
            else s.push_back(str[i]);
        }
        cout << "Case #" << cn << ": ";
        for(auto&c : s){
            cout << c;
        }
        cout << '\n';
    }
    return 0;
}
