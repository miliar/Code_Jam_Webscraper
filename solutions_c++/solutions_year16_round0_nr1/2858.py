#include <iostream>
#include <cmath>

using namespace std;

bool seen[10];

void see(int n) {
    while (n > 0) {
        seen[n % 10] = true;
        n /= 10;
    }
}

bool allSeen() {
    for (int i = 0; i < 10; i++) {
        if (!seen[i]) {
            return false;
        }
    }
    
    return true;
}

int main() {
    int t;
    cin >> t;
    
    for (int i = 0; i < t; i++) {
        for (int j = 0; j < 10; j++) seen[j] = false;
        
        bool yes = false;
        int n, f;
        cin >> n;
        
        for (int j = 1; j < pow(10, (floor(log10(n))) + 2); j++) {
            see(n * j);
            if (allSeen()) {
                yes = true;
                f = n * j;
                break;
            }
        }
        
        cout << "Case #" << i + 1 << ": ";
        if (yes) {
            cout << f << endl;
        } else {
            cout << "INSOMNIA" << endl;
        }
            
    }
    
    return 0;
}