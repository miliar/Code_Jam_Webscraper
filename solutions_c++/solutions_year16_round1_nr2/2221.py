#include <iostream>

using namespace std;

int main() {
    
    int t, n;
    
    int a[100][50];
    int used[100];
    int res[50];
    
    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    
    for (int i = 1; i <= t; ++i) {
        
        
        cin >> n;
        
        for (int k = 0; k < n; k++)
            res[k] = -1;
        
        for (int j = 0; j < 2*n-1; j++) { // lines
            for (int k = 0; k < n; k++) { // numbers in lines
         
                used[j] = 0;
                cin >> a[j][k];
            }
            
        }
        
        int line = 0;
        
        int k, num, j;
        int min;
        for (k = 0; k < n; k++) {
            min = 10000;
            for (int j = 0; j < 2*n-1; j++) {
                if (used[j] == 0)
                    min = a[j][k] < min ? a[j][k] : min;
            }
            
            int cnt = 0;
            for (j = 0; j < 2*n-1; j++) {
                if (used[j] == 0) {
                    if (a[j][k] == min) {
                        line = j;
                        used[j] = 1;
                        cnt++;
                    }
                }
            }
            if (cnt == 1)
                break;
        }
        
        
        for (int k = 0; k < 100; k++)
            used[k] = 0;
        
        num = k;
        res[num] = a[line][num];
//        res[0] = a[line][0];
        

        for (int k = 0; k < n; k++) {
            int cmp = a[line][k];
            int tmp[2];
            int cnt = 0;
            min = 10000;
            for (int j = 0; j < 2*n-1; j++)
                if (used[j] == 0)
                    min = a[j][k] < min ? a[j][k] : min;
                
            for (j = 0; j < 2*n-1; j++)
                if (used[j] == 0)
                    if (a[j][k] == min){
                        used[j] = 1;
                        tmp[cnt] = j;
                        cnt++;
                    }
            

            if (res[k] == -1) {
                
                
//                cout << "k: " << k << ' ' << a[tmp[0]][num] << ' ' << a[tmp[1]][num] << ' ' << cmp << endl;
                
                if (cmp == a[tmp[0]][num])
                    res[k] = a[tmp[1]][num];
                else
                    res[k] = a[tmp[0]][num];
                
                
            }
            
            
            
        }
        
        
            
        
        
//        cout << "Case #" << i << ": " << num << ' ' << line << endl;
        cout << "Case #" << i << ": ";
/*
        for (int j = 0; j < 2*n-1; j++) { // lines
            for (int k = 0; k < n; k++) { // numbers in lines
                
                cout << a[j][k] << '\t';
            }
            cout << endl;
        }
        
        cout << endl;
*/
        for (int k = 0; k < n; k++) { // numbers in lines
            cout << res[k] << ' ';
        }
        cout << endl;
    }
}