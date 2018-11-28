#include <iostream>
#include <fstream>
#include <vector>
#include <stack>
#include <string>
 
using namespace std;

int main()
{
    int t;
    string s;
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    for(int i = 0; i < t; ++i){
        int len, sum = 0, res = 0;
        cin >> len;
        cin >> s;
        sum = s[0] - '0';
        for(int j = 1; j < s.size(); ++j){
            res += max(0, j - sum);
            sum += s[j] - '0' + max(0, j - sum);
        }
        cout << "Case #" << i+1 << ": " << res << '\n';
        //cout << s << " " << res << '\n';
    }
    
    return 0;
}