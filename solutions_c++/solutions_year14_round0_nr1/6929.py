#include <iostream>

using namespace std;

int T, u[16], a1[16], a2[16];

int main() {
    cin >> T;
    for(int t = 0; t < T; ++ t) {
        int r1;
        int count = 0;
        int last;
        cin >> r1;
        r1 --;
        for(int i = 0; i < 4; ++ i)
            for(int j = 0; j < 4; ++j) {
                int a;
                cin >> a;
                a --;
                if(r1 == i)
                    u[a] = 1;
                else
                    u[a] = 0;
            }
        int r2;
        cin >> r2;
        r2 --;
        for(int i = 0; i < 4; ++ i)
            for(int j = 0; j < 4; ++ j) {
                int a;
                cin >> a;
                a --;
                if(r2 == i) {
                    u[a] ++;
                    if(u[a] == 2) {
                        count ++;
                        last = a + 1;
                    }
                }
            }
        cout << "Case #" << t + 1 << ": ";
        if(count == 0)
            cout << "Volunteer cheated!\n";
        if(count == 1)
            cout << last << '\n';
        if(count > 1)
            cout << "Bad magician!\n";
    }

    return 0;
}
