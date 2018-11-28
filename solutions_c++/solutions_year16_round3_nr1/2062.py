#include <iostream>
#include <stdlib.h>     /* atoi */

using namespace std;
int main() {
    int t, n;
    int p[26];
    string res;
    
    cin >> t;

    for (int i = 1; i <= t; ++i) {
        
        res.clear();
        cin >> n;
        
        
        for (int j = 0; j < n; ++j) {
       
            cin >> p[j];
        }
        
        cout << "Case #" << i << ": " ;
        
        int sum = 0;
        for (int j = 0; j < n; ++j) {
//            cout << p[j] << endl;
            sum += p[j];
        }
        
        do {

//            cout << 's' << sum << endl;
        
        int max = *std::max_element(p,p+n);
        
        int pos1 = 0;
        for (int j = 0; j < n; ++j) {
            
            if (p[j] == max) {
                pos1 = j;
                break;
            }
        }
        
//        cout << "p1: " << pos1;
        
        int pos2 = pos1;
        for (int j = pos1+1; j < n; ++j) {
            
            if (p[j] == max) {
                pos2 = j;
                break;
            }
        }
            
        int pos3 = pos2;
           for (int j = pos3+1; j < n; ++j) {
                
               if (p[j] == max) {
                    pos3 = j;
                    break;
                }
          }
            
            if (pos3 != pos2) {
                pos2 = pos1;
            }
            
        
//        cout << "p2: " << pos2;
            char out1 = 'A' + pos1;
            char out2 = 'A' + pos2;
        
        if (pos1 == pos2) {
            cout << out1 << "\t";
            p[pos1]--;
        } else {
            cout << out1 << out2<< "\t";
            p[pos1]--;
            p[pos2]--;
        }
            
             sum = 0;
            for (int j = 0; j < n; ++j) {
//                cout << p[j] << endl;
                sum += p[j];
            }
        
        } while (sum != 0);
        
        
        
        
        
        
        cout << endl;
    }
}