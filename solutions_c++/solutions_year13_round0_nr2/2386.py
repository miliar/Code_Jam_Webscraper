#include <iostream>
#include <iterator>
#include <set>

using namespace std;

int d[128][128];

int main(int argc, char* argv[])
{
    int T, N, M;
    cin >> T;
    for (int t = 0; t != T; ++t) {
        cin >> N >> M;
        for (int y = 0; y != N; ++y)
            for (int x = 0; x != M; ++x)
                cin >> d[y][x];

        set<pair<int, int> > sLR, sTB;

        for (int y = 0; y != N; ++y) {
            int maxHL = 0;
            int maxHR = 0;
            for (int x = 0; x != M; ++x) {
                if (d[y][x] < maxHL)
                    sLR.insert(make_pair(y, x));
                else
                    maxHL = d[y][x];

                int x1 = M - 1 - x;
                if (d[y][x1] < maxHR)
                    sLR.insert(make_pair(y, x1));
                else
                    maxHR = d[y][x1];
            }
        }

        for (int x = 0; x != M; ++x) {
            int maxHT = 0;
            int maxHB = 0;
            for (int y = 0; y != N; ++y) {
                if (d[y][x] < maxHT)
                    sTB.insert(make_pair(y, x));
                else
                    maxHT = d[y][x];

                int y1 = N - 1 - y;
                if (d[y1][x] < maxHB)
                    sTB.insert(make_pair(y1, x));
                else
                    maxHB = d[y1][x];
            }
        }

        set<pair<int, int> > sLRTB;

        set_intersection(sLR.begin(), sLR.end(),
                         sTB.begin(), sTB.end(),
                         insert_iterator<set<pair<int, int> > >(sLRTB, sLRTB.end()));

        if (sLRTB.empty())
            cout << "Case #" << (t + 1) << ": YES\n";
        else
            cout << "Case #" << (t + 1) << ": NO\n";
    }
    return 0;
}


