//
//  MagicTrick.cpp
//  
//
//  Created by John Nevard on 4/11/14.
//
//

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int nc;
    cin >> nc;
    for (int i = 1; i <= nc; ++i) {
        int a[4][4], b[4][4], r1, r2;
        cin >> r1;
        for (int r = 0; r < 4; ++r)
            for (int c = 0; c < 4; ++c)
                cin >> a[r][c];
        cin >> r2;
        for (int r = 0; r < 4; ++r)
            for (int c = 0; c < 4; ++c)
                cin >> b[r][c];
        --r1;
        --r2;
        int nf = 0;
        int answer = -1;
        for (int c1 = 0; c1 < 4; ++c1)
            for (int c2 = 0; c2 < 4; ++c2)
                if (a[r1][c1] == b[r2][c2])
                    if (++nf == 1)
                        answer = a[r1][c1];
        cout << "Case #" << i << ": ";
        if (!nf)
            cout << "Volunteer cheated!" << '\n';
        else if (nf > 1)
            cout << "Bad magician!" << '\n';
        else
            cout << answer << '\n';
    }
    cout.flush();
    return 0;
}