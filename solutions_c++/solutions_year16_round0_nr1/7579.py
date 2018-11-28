#include <bits/stdc++.h>
using namespace std;

int main (int argc, char** argv) {
    int t, n, res;
    map<int,int> occur;
    
    cin >> t;
    for (int cur = 1; cur <= t; cur++) {
        occur.clear();
        cin >> n;
        
        cout << "Case #" << cur << ": ";
        
        if (n == 0) {
            cout << "INSOMNIA" << endl;
            continue;
        }
        
        for (res = n; occur.size() < 10; res += n) {
            int tmp = res;
            while (tmp != 0) {
                occur[tmp%10]++;
                tmp /= 10;
            }
        }
        
        cout << res-n << endl;
    }
    
    return 0;
}
