#include <iostream>
#include <queue>

using namespace std;

int main() {
    int cases;
    cin >> cases;
    for (int test = 1; test <= cases; test++) {
        int tabTempl[1001] = {0};
        int tabSize = 0;
        int diners, pancakesNo;
        cin >> diners;
        for (int i = 0; i < diners; i++) {
            cin >> pancakesNo;
            tabTempl[pancakesNo]++;
            if (pancakesNo > tabSize)
                tabSize = pancakesNo;
        }
        int result = tabSize;
        
        for (int aaa = 0; aaa < 2; aaa++) {
            int tab[1001] = {0};
            for (int i = 0; i <= tabSize; i++) {
                tab[i] = tabTempl[i];
            }
            
           // for (int i = 0; i < 10; i++) {
         //       cout << "tab[" << i << "]: " << tab[i] << endl;
       //     }
        
            int penalties[10] = {0};
            for (int i = 9; i > 0; i--) {
                
                int dno = tab[i];
                penalties[i-1] = penalties[i] + dno;
                switch (i) {
                    case 9:
                        if (aaa == 0) {
                            tab[5] += dno;
                            tab[4] += dno;
                        }
                        else {
                            tab[6] += dno;
                            tab[3] += dno;
                        }
                        break;
                    case 8:
                        tab[4] += 2*dno;
                        break;
                    case 7:
                        tab[4] += dno;
                        tab[3] += dno;
                        break;
                    case 6:
                        tab[3] += 2*dno;
                        break;
                    case 5:
                        tab[2] += dno;
                        tab[3] += dno;
                        break;
                    case 4:
                        tab[2] += 2*dno;
                        break;
                    case 3:
                        tab[2] += dno;
                        tab[1] += dno;
                        break;
                    case 2:
                        tab[1] += 2*dno;
                        break;
                    case 1:
                        break;
                }
            }
            
         //   for (int i = 0; i < 10; i++) {
        //        cout << "pen[" << i << "]: " << penalties[i] << endl;
      //      }
            
            for (int i = tabSize; i > 0; i--) {
                int can = i + penalties[i];
                if (can < result)
                    result = can;
            }
        }
        
        cout << "Case #" << test << ": " << result << endl;
    }
}
