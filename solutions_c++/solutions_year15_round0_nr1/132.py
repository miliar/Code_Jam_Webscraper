#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <cstdlib>
#include <cmath>
#include <string>
#include <algorithm>
#include <cstdio>
#include <ctime>

using namespace std;


int main(int argc, char **argv){
    freopen("/Users/Arseniy/All/Int/input.txt", "r", stdin);
    freopen("/Users/Arseniy/All/Int/int/output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int o=0;o<t;o++){
        cout << "Case #" << o+1 << ": ";
        int sm;
        string s;
        cin >> sm;
        cin >> s;
        int ans = 0;
        int num = s[0] - '0';
        for (int i=1;i<sm+1;i++){
            if (s[i] != '0'){
                if (i > num){
                    ans += i - num;
                    num += i - num;
                }
                num += s[i]-'0';
            }
        }
        cout << ans << endl;
    }
    
    return 0;
}