#include <iostream>

using namespace std;

string arra[10] = {"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};

int main() {
    
    int t,a=0;
    cin >> t;
    int x = 1;
    string text;
    
    while(t){
        
        cin >> text;
        cout << "Case #" << x++ << ": ";
        
        int array[40] = {0};
        int sayma[10] = {0};
        
        a=0;
        
        while (text[a] != '\0') {
            
            array[text[a]-'A']++;
            
            if (text[a]== 'Z') {
                sayma[0]++;
                
            } else if (text[a]== 'G') {
                sayma[8]++;
                
                
            } else if (text[a]== 'X') {
                sayma[6]++;
                
                
            } else if (text[a]== 'W') {
                sayma[2]++;
                
                
            } else if (text[a]== 'U') {
                sayma[4]++;
                
            }
            
            a++;
        }
        
        for (int a = 0; a <= 8; a+=2) {
            
            int miktar = sayma[a];
            
            while (miktar > 0) {
                
                for (int b = 0; b < arra[a].size(); b++) {
                    array[arra[a][b]-'A']--;
                    
                    for (int x = 0; x < text.size(); x++) {
                        if (text[x]==arra[a][b]) {
                            text[x] = 'Q';
                            break;
                        }
                    }
                }
                
                miktar--;
            }
        }
        
        a=0;
        
        while (text[a] != '\0') {
            
            if (text[a]== 'O') {
                sayma[1]++;
                
            } else if (text[a]== 'R') {
                sayma[3]++;
                
            } else if (text[a]== 'F') {
                sayma[5]++;
                
            } else if (text[a]== 'S') {
                sayma[7]++;
                
            }
            
            a++;
        }
        
        for (int a = 1; a < 10; a+=2) {
            
            int miktar = sayma[a];
            
            while (miktar > 0) {
                
                for (int b = 0; b < arra[a].size(); b++) {
                    array[arra[a][b]-'A']--;
                    
                    for (int x = 0; x < text.size(); x++) {
                        if (text[x]==arra[a][b]) {
                            text[x] = 'Q';
                            break;
                        }
                    }
                }
                
                miktar--;
            }
        }
        
        a=0;
        
        while (text[a] != '\0') {
            
            if (text[a]== 'I') {
                sayma[9]++;
                
            }
            
            a++;
        }
        
        for (int a = 0; a <= 9; a++) {
            while (sayma[a]>0) {
                cout << a;
                sayma[a]--;
            }
        }
        
        t--;
        cout << endl;
    }
    
    
    return 0;
}
