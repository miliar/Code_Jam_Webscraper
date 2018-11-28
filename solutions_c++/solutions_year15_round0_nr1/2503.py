#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    fstream cin, cout;
    cin.open("input.txt", ios_base::in);
    cout.open("output.txt", ios_base::out);
    
    int t, ti;
    int s, a[2000], res, bag, inc;
    string str;
    int i, j;
    
    cin >> t;
    for (ti = 1; ti <= t; ++ti) {
        res = bag = 0;
        cin >> s >> str;
        for (i = 0; i <= s; ++i) {
            a[i] = str[i] - '0';
        }
        
        for (i = 0; i <= s; ++i) {
            inc = 0;
            if ((i > bag) && (a[i] != 0)) inc = i - bag;
            res += inc;
            bag += a[i] + inc;
            //cout << "DDD i=" << i << " bag=" << bag << " res=" << res << endl;
        }
        
        cout << "Case #" << ti << ": " << res << endl;
    }
    cout.close();
}
