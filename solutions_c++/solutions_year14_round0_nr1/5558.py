#include <iostream>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int test=1; test <= T; test++) {
        int n1[4], n2[4];
        int a;
        int r1, r2;
        int c;
        
        cin >> r1;
        for (int r=1; r <= 4; r++)
            if (r == r1)
               cin >> n1[0] >> n1[1] >> n1[2] >> n1[3];
            else
                cin >> a >> a >> a >> a;
        
        cin >> r2;
        for (int r=1; r <= 4; r++)
            if (r == r2)
               cin >> n2[0] >> n2[1] >> n2[2] >> n2[3];
            else
                cin >> a >> a >> a >> a;
        
        int res = 0;
        for (int i=0; i<4; i++) {
            for (int j=0; j<4; j++) {
                if (n1[i] == n2[j]) {
                   res++;
                   c = n1[i];
                }
            }
        }
        cout << "Case #" << test << ": ";
        if (res == 1)
           cout << c << endl;
        else if (res == 0)
           cout << "Volunteer cheated!\n";
        else
            cout << "Bad magician!\n";
    }

    return 0;
}
