#include <bits/stdc++.h>
using namespace std;

string revPancakes(string s, int w) {
    for(int f = 0; f<w; ++f) {
        if(s[f] == '+') {
            s[f] = '-';
        }
        else {
            s[f] = '+';
        }
    }
    return s;
}

int main() {
    
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int t, i;
    cin >> t;
    for(i = 1; i <= t; ++i) {
        
        string pancakes;
        cin >> pancakes;
        int len = pancakes.size();
        int mark = len, c = 0, sol = 0;
        for(int k = len-1; k>=0; --k) {
            if(pancakes[k] == '-') {
                c++;
            }
            else {
                if(c) {
                    pancakes = revPancakes(pancakes, mark);
                    sol++;
                    k++;
                }
                mark = k;
                c = 0;
            }
        }
        
        if(c) {
            pancakes = revPancakes(pancakes, mark);
            sol++;
        }
        
        cout << "Case #" << i << ": " << sol << endl;
    }
    
	return 0;
}
