#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <iomanip>

using namespace std;

int main(int argc, const char * argv[]) {
    
    int testCases;
    
    cin >> testCases;
    
    for(int testCase = 1; testCase <= testCases; ++testCase) {
        cout << "Case #" << testCase << ": " ;
        
        
        string s;
        cin >> s;
        string ans = "";
        for(int i = 0; i < s.length(); i++) {
            ans = max(s[i] + ans, ans + s[i]);
        }
        
        cout << ans << endl;
        
        //
        
    }
    
    return 0;
}
