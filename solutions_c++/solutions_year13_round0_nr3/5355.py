#include <iostream>

using namespace std;

int T, A, B, count;
int known[6] = {1, 4, 9, 121, 484, 10000};

int main()
{
    freopen("input.in", "r", stdin);
    freopen("outputl.out", "w", stdout);

    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cin >> A >> B;
        count = 0;
        for (int j = 0; j < 6; ++j) {
            if (A <= known[j])
                ++count;
            if (B < known[j]) {
                --count;
                break;
            }
        }

        cout << "Case #" << i << ": "
                << count << endl;

    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}

