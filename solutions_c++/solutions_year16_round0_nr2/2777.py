#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>

using namespace std;

int main() {
    
    freopen("pancakes.in", "r", stdin);
    freopen("pancakes.out", "w", stdout);

    int N;
    string str;
    cin >> N;
    for(int i = 0; i < N; i++) {
        int ans = 0;
        cout << "Case #" << i+1 << ": ";
        cin >> str;
        for(int j = 0; j < str.length()-1; j++) {
            if(str[j] != str[j+1])
                ans++;
        }
        if(str[str.length()-1] == '-')
            ans++;
        cout << ans << endl;
        //cout << str.length() << endl;
    }
    
    return 0;
}
