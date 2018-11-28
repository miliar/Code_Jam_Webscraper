#include <iostream>

using namespace std;

int main()
{

    int t;
    cin >> t;
    for (int case_num = 1; case_num <= t; ++case_num) {
        int a[17];
        for (int i = 1; i <= 16; ++i)
            a[i] = 0;

        int c;
        cin >> c;
        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j) {
                int x;
                cin >> x;
                if (c == i + 1)
                    a[x]++;
            }
        int r;
        cin >> r;
        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j) {
                int x;
                cin >> x;
                if (r == i + 1)
                    a[x]++;
            }
        int res = 0;
        for (int i = 1; i <= 16; ++i)
            if (a[i] == 2) {
                if (res == 0)
                    res = i;
                else
                    res = -1;
            }

        cout << "Case #" << case_num << ": ";
        if (res == -1)
            cout << "Bad magician!";
        else if (res == 0)
            cout << "Volunteer cheated!";
        else
            cout << res;
        cout << "\n";
    }

    return 0;
}
