#include <bits/stdc++.h>
using namespace std;

bool check(string pancakes) {
    for (int i = 0; i < pancakes.size(); i++)
        if (pancakes[i] == '-') 
            return false;
    return true;
}

int main (int argc, char** argv) {
    int t, res;
    string pancakes;
    
    cin >> t;
    for (int cur = 1; cur <= t; cur++) {
        cin >> pancakes;
        
        cout << "Case #" << cur << ": ";
        
        res = 0;
        
        int endp = pancakes.size()-1;
        while (pancakes[endp] == '+' && endp >= 0) endp--;
        pancakes.resize(endp+1);
        
        while (check(pancakes) == false) {
            res++;
            if (pancakes[0] == '-') {
                reverse(pancakes.begin(), pancakes.end());
                for (int i = 0; i < pancakes.size(); i++)
                    pancakes[i] = (pancakes[i] == '+' ? '-' : '+');
                int endp = pancakes.size()-1;
                while (pancakes[endp] == '+' && endp >= 0) endp--;
                pancakes.resize(endp+1);
            } else {
                for (int i = 0; i < pancakes.size() && pancakes[i] == '+'; i++)
                    pancakes[i] = '-';
            }
        }
        cout << res << endl;
    }
    
    return 0;
}
