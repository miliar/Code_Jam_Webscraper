#include <iostream>
#include <cstring>
using namespace std;

bool D[10];

int main() {
    int tests; cin >> tests;
    for(int test=1; test<=tests; test++) {
        memset(D, 0, sizeof D);
        
        int n; cin >> n;
        int seen = 0;
        int answer = -1;
        
        for(int i=1; i<1000; i++) {
            int x = i*n;
            while(x) {
                if (!D[x%10]) seen++;
                D[x%10] = true;
                x/=10;
            }
            
            if (seen == 10) {
                answer = i*n;
                break;
            }
        }
        
        cout << "Case #" << test << ": ";
        if (answer == -1)
            cout << "INSOMNIA" << endl;
        else
            cout << answer << endl;
    }
}
