#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>

#define f first
#define s second

using namespace std;




int main()
{
    freopen("a.txt", "r", stdin);
    freopen("aout.txt", "w", stdout);
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i)
    {
        int N1, N2;
        int A1[4][4];
        int A2[4][4];
        cin >> N1;
        for (int j = 0; j < 4; ++j)
        {
            for (int k = 0; k < 4; ++k)
            {
                cin >> A1[j][k];
            }
        }
        set <int> Ans;
        for (int j = 0; j < 4; ++j)
        {
            Ans.insert(A1[N1 - 1][j]);
        }
        cin >> N2;
        for (int j = 0; j < 4; ++j)
        {
            for (int k = 0; k < 4; ++k)
            {
                cin >> A2[j][k];
            }
        }
        int Q = 0;
        int num;
        for (int j = 0; j < 4; ++j)
        {
            if (Ans.count(A2[N2 - 1][j]))
            {
                num = A2[N2 - 1][j];
                ++Q;
            }
        }
        if (Q > 1)
        {
            cout << "Case #"<< i + 1 <<": Bad magician!" << endl;
        }
        if (Q == 1)
        {
            cout << "Case #"<< i + 1 << ": "<< num << endl;
        }
        if (Q== 0)
        {
            cout << "Case #" << i + 1 <<": Volunteer cheated!" << endl;
        }
    }
    return 0;
}
