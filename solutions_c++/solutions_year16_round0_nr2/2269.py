

#include <iostream>
#include <vector>
#include <string>
#include <set>

using namespace std;



int main(int argc, const char * argv[]) {
    int T;
    cin >> T;
    for(int tt = 1; tt <= T; ++tt){
        string s;
        cin >> s;
        int ret = 0;
        while(s.find("-") != string::npos){
            ++ret;
            int p = 0;
            while(p < s.size() && (p == 0 || s[p-1] == s[p])){
                ++p;
            }
            for(int i=0; i<p; ++i){
                s[i] = (s[i] == '+' ? '-' : '+');
            }
        }
        
        cout << "Case #" << tt << ": " << ret << endl;
    }
    return 0;
}
