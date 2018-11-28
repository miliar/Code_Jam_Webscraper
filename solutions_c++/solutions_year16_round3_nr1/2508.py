#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large-result.txt", "w", stdout);

    int T; cin >> T;

    for (int t = 1; t <= T; t++) {
        int N; cin >> N;

        int P1 = 0, P2 = 0, P_temp;
        int i1 = 0, i2 = 1;

        vector<int> parties(N, 0);

        cin >> P1; cin >>P2;
        parties[0] = P1; parties[1] = P2;

        if (P1 < P2) { P_temp = P2; P2 = P1; P1 = P_temp ; i1 = 1; i2 = 0; }

        int P;

        for (int i = 2; i < N; i++) {
            cin >> P;
            if (P >= P1) { P2 = P1; P1 = P; i2 = i1; i1 = i; }
            else if (P > P2) { P2 = P; i2 = i; }
            parties[i] = P;
        }

        //cout << "P1 = " << P1 << ", P2 = " << P2 << "i1 = " << i1 << ", i2 = " << i2 << endl;



        cout << "Case #" << t << ": ";

        while (P1 > P2) {
            cout << char('A' + i1) << " ";
            P1--;
        }

        for (int i = 0; i < N; i++) {
            if (i != i1 && i != i2) {
                for (int j = 0; j < parties[i]; j++)
                    cout << char('A'+i) << " ";
            }
        }

        for (int i = 0; i < P2; i++) {
            cout << char('A' + i1) << char('A' + i2) << " ";
        }

        cout << endl;




    }

    return 0;
}
