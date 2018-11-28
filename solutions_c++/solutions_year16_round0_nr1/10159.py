
#include <bits/stdc++.h>

#define MAX 10

using namespace std;

int toNumber(string s){
    int n;
    if (!(istringstream(s) >> n)) n = 0;
    return n;
}

string toString(int n){
    return static_cast<ostringstream*>( &(ostringstream() << n) )->str();
}

int main () {
    ios_base::sync_with_stdio(false);
    
    int t, n, cubeta[MAX], idx, flag;
    string s;
 
    cin >> t;
    
   for (int i = 1; i <= t; i++) {
        memset(cubeta, 0, sizeof(cubeta));
        
        idx = 1;
        cin >> n;
        
        if (n == 0) {
            cout << "Case #" << idx << ": INSOMNIA\n";
            continue;
        }
        
       
        
        while(1) {
            
             s = toString(n * idx++);
            
            flag = 0;
            for (int j = 0; j < s.size(); j++)
                cubeta[s[j] - '0'] = 1;
            for (int j = 0; j < 10; j++)
                if (cubeta[j] == 0) {
                    flag = 1; break;
                }
            
            //cout << s << '\n';
            
            if (flag == 0) { cout << "Case #" << i << ": " << n * (idx - 1) << '\n'; break; }
        
        }
        
    }
    
    return 0;
}