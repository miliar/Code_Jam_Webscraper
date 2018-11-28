#include <iostream>
#include <algorithm>
#include <vector>
#include <array>

using namespace std;

void
process(int test_id)
{
    cerr << "Processing #" << test_id << ": ";
    int ans1 = 0, ans2 = 0;
    array< array< int, 4 >, 4 > board1 = {}, board2 = board1;
    array< int, 16 > ok = {};
    cin >> ans1;
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            cin >> board1[i][j];
        }
    }
    cin >> ans2;
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            cin >> board2[i][j];
        }
    }
    for (int j = 0; j < 4; ++j) {
        ok[board1[ans1 - 1][j] - 1]++;
        ok[board2[ans2 - 1][j] - 1]++;
    }
    vector< int > res;
    res.reserve(4);
    for (int i = 0; i < 16; ++i) {
        if (ok[i] == 2) {
            res.push_back(i + 1);
        }
    }
    cout << "Case #" << test_id << ": ";
    if (res.size() == 0U) {
        cout << "Volunteer cheated!";
    } else if (res.size() > 1U) {
        cout << "Bad magician!";
    } else {
        cout << res.front();
    }
    cout << endl;
    cerr << "ok" << endl;
}

int
main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        process(i);
    }
    return 0;
}
