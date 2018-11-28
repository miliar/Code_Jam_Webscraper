#include <iostream>
#include <string>

using namespace std;

int main() {
    
    int t, uzunluk, kullan;
    int caseOrder = 1;
    cin >> t;
    string arr;
    
    while (t--) {
        cin >> arr;
        uzunluk = int(arr.length());
        int miktar = 0;
        
        if (uzunluk == 1) {
            if (arr == "+") {
                cout << "Case #" << caseOrder++ << ": 0" << endl;
            } else {
                cout << "Case #" << caseOrder++ << ": 1" << endl;
            }
            
            continue;
        
        } else {
            
            kullan = uzunluk-1;
            
            while (kullan > 0) {
                
                while (arr[kullan] == '+') {
                    kullan--;
                    uzunluk--;
                }
                
                if (uzunluk == 0) {
                    break;
                }
                
                for (int x = 0; x <= kullan; x++) {
                    if (arr[x] == '+') {
                        arr[x] = '-';
                    } else {
                        arr[x] = '+';
                    }
                }
                
                miktar++;
            }
            
            cout << "Case #" << caseOrder++ << ": "<< miktar << endl;
            miktar = 0;
        }
    }

    return 0;
}
