#include <cstdio>
#include <iostream>
#include <cstdlib>

using namespace std;

int main()
{
    freopen("A-small-attempt2.in.txt","r",stdin);
    freopen("output2.txt","w",stdout);
    int t, ans1, ans2;
    int grid[4][4];

    cin >> t;
    for(int i = 1;i <= t;i++) {
        cin >> ans1;

        int A, B, C;

        A = B = C = 0;
        for(int j = 0;j < 4;j++) {
            for(int k = 0;k < 4;k++) {
                cin >> grid[j][k];
                if(j+1 == ans1) {
                    A |= (1 << grid[j][k]);
                }
            }
        }

        cin >> ans2;

        for(int j = 0;j < 4;j++) {
            for(int k = 0;k < 4;k++) {
                cin >> grid[j][k];
                if(j+1 == ans2) {
                    B |= (1 << grid[j][k]);
                }
            }
        }

        C = A & B;
        cout << "Case #" << i << ": ";
        //Check if empty
        if(C == 0) {
            cout << "Volunteer cheated!\n";
        } else if((C > 0) && (C & (C-1)) != 0) {
            cout << "Bad magician!\n";
        }//multiple elements

        else {
            int low = __builtin_ctz(C);
            cout << low << endl;
        }

    }

    return 0;
}
