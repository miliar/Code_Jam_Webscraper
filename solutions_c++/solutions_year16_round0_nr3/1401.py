#include <iostream>
#include <map>
#include <bitset>
#include <cmath>

using namespace std;

#define ll long long

int n, j, t;

int main() {
    cin >> t;
    
    for (int i = 1; i <= t; i++) {
        cin >> n >> j;
        cout << "Case #"<< i<<": "<<endl;
        int cnt = 0;        
        
            for (int a = 2; a <= n/2; a++)
                for (int b = a+1; b <= n/2; b++)
                    for (int c = 1;c <= n/2-1; c++)
                        for (int d = c+1; d <= n/2-1; d++) {
                            if (n == 16) {
                            bitset<16> x;
                            x[0] = 1;
                            x[15] = 1;
                            x[(a-1)*2] = 1;
                            x[(b-1)*2] = 1;
                            x[2*c-1] = 1;
                            x[2*d-1] = 1;
                    
                            cnt++;
                             
                            cout << x<< " 3 2 3 2 7 2 3 2 3" << endl;
                            if (cnt == j)
                                return 0; 
                            } else {
                            bitset<32> x;
                            x[0] = 1;
                            x[31] = 1;
                            x[(a-1)*2] = 1;
                            x[(b-1)*2] = 1;
                            x[2*c-1] = 1;
                            x[2*d-1] = 1;
                    
                            cnt++;
                             
                            cout << x<< " 3 2 3 2 7 2 3 2 3" << endl;
                            if (cnt == j)
                                return 0;
                            }
                        }
    
    }
    return 0;
}   
