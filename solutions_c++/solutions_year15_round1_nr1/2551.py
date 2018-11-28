#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int T;
    cin >> T;

    for (int t = 1; t <= T; ++t)
    {
        int N;
        cin >> N;
        vector<int> mushrooms(N, 0);
        for (int i = 0; i < N; ++i) cin >> mushrooms[i];

        int eaten1 = 0;
        for (int i = 1; i < N; ++i) {
            if (mushrooms[i - 1] > mushrooms[i]) {
                eaten1 += mushrooms[i - 1] - mushrooms[i];
                //cout << "out1: eaten1=" << eaten1 << endl;
            }
        }


        int rate = 0;
        for (int i = 1; i < N; ++i) if (mushrooms[i-1] > mushrooms[i]) rate = max(rate, mushrooms[i-1] - mushrooms[i]);
        //cout << "rate=" << rate << endl;
        int eaten2 = 0;
        int total = 0;
        for (int i = 0; i < N-1; ++i)
        {
            int m = min(rate, mushrooms[i]);
            eaten2 += m;
        }

        cout << "Case #" << t << ": " << eaten1 << " " << eaten2 << endl;
    }

    return 0;
}
