#include "string"
#include "iostream"
#include "cmath"
using namespace std;

int main() {
    int T;
    cin >> T;
    int A, B;
    int result;

    for (int k=0; k<T; k++) {
        cin >> A >> B;
        // 1, 4, 9, 121, 484
        // 1, 2, 3, 11, 22
        if (A==1) {
            if (B<4) {result = 1;}
            else if (B<9) {result = 2;}
            else if (B<121) {result = 3;}
            else if (B<484) {result = 4;}
            else {result = 5;}
        }
        else if (A<=4) {
            if (B<4) {result = 0;}
            else if (B<9) {result = 1;}
            else if (B<121) {result = 2;}
            else if (B<484) {result = 3;}
            else {result = 4;}
        
        }
        else if (A<=9) {
            if (B<9) {result = 0;}
            else if (B<121) {result = 1;}
            else if (B<484) {result = 2;}
            else {result = 3;}
        }
        else if (A<=121) {
            if (B<121) {result = 0;}
            else if (B<484) {result = 1;}
            else {result = 2;}
        }
        else if (A<=484) {
            if (B<484) {result = 0;}
            else {result = 1;}
        }
        else {
            result = 0;
        }
        cout << "Case #" << k+1 << ": " << result << endl;
    
    }
    return 0;
}
