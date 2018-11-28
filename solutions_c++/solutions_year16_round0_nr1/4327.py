#include <iostream>
using namespace std;

int main() {
    int n,t;
    cin >> t;
    for(int a = 1; a <= t; a++) {
        cin >> n;
        if(n == 0) {
            cout << "Case #" << a << ": " << "INSOMNIA" << endl;
            continue;
        }
        bool* seen = new bool[10];
        for(int i = 0; i < 10; i++) {
            seen[i] = false;
        }
        for(long i = n; ; i += n) {
             long temp = i;
             while(temp > 0) {
                 int r = temp % 10;
                 seen[r] = true;
                 temp /= 10;
             }
             bool seenAll = true;
             for(int b = 0; b < 10; b++) {
                 if(!seen[b]) {
                     seenAll = false;
                     break;
                 }
             }
             if(seenAll) {
                 cout << "Case #" << a << ": " << i << endl;
                 break;
             }
        }
    }
    return 0;
}