#include<iostream>
#include<cstring>
using namespace std;
string biao = "111011111011011011001011111001101000011011000010";
int main(){
    int Tcase = 0;
    cin >> Tcase;
    for (int casenow = 1; casenow <= Tcase; casenow++) {
        int x,r,c;
        cin >> x >> r >> c;
        if (x == 1) {
            cout << "Case #" << casenow << ": " << "GABRIEL" << endl;
        }else{
            if (biao[(r-1)*12+(c-1)*3+x-2] == '1') {
                cout << "Case #" << casenow << ": " << "RICHARD" << endl;
            }else{
                cout << "Case #" << casenow << ": " << "GABRIEL" << endl;
            }
        }
        
    }
    return 0;
}
