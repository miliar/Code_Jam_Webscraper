#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for(int r=0;r<T;r++){
        string s;
        int k;
        cin >> s >> k;
        int count = 0;
        for(int i=0;i<=s.size()-k;i++){
            if(s[i] == '-'){
                for(int j=i;j<i+k;j++){
                    if(s[j] == '-') s[j] = '+';
                    else s[j] = '-';
                }
               // cout << s << endl;
                count ++;
            }
        }
        
        bool flag = true;
        for(int i=0;i<s.size();i++) if(s[i] == '-') flag = false;
        //cout << s << endl;
        if(!flag) cout << "Case #" << r+1 << ": IMPOSSIBLE" << endl;
        else cout << "Case #" << r+1 << ": " << count << endl;
    }
    return 0;
}
