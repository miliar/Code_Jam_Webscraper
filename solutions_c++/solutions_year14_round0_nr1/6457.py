//#include <iostream>
#include <fstream>
using namespace std;

ifstream cin("A-small-attempt0.in");
ofstream cout("A-small.out");

int main() {
    int T;
    cin >> T;
    int A[4][4];
    int B[4][4];
    int c0,c1;
    for (int t=0; t<T; t++) {
       cout << "Case #" << t+1 << ": ";
       cin >> c0; c0--;
       for (int i=0; i<4; i++) for (int j=0; j<4; j++) cin >> A[i][j];
       cin >> c1; c1--;
       for (int i=0; i<4; i++) for (int j=0; j<4; j++) cin >> B[i][j];
       int n2=0, cn2=-1;
       for (int i=0; i<4; i++) {
        for (int j=0; j<4; j++) {
            if (A[c0][i] == B[c1][j]) { n2++; cn2=A[c0][i]; }
        }
       }
       if (n2 == 0) cout << "Volunteer cheated!" << endl;
       else if (n2 == 1) cout << cn2 << endl;
       else cout << "Bad magician!" << endl;
    }
return 0;
}
