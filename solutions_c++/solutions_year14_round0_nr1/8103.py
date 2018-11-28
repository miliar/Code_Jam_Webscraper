#include <iostream>
#include <set>
#include <algorithm>
#include <iterator>

using namespace std;



int main() {
    int T;
    cin >> T;
    for (int t=0; t<T; ++t) {
        set<int> s1, s2;
        int ans1, ans2;
        cin >> ans1;

        int M1[4][4];
        for (int row=0; row < 4; ++row) {
            for (int col=0; col < 4; ++col) {
                cin >> M1[row][col];
            }
        }

        cin >> ans2;
        int M2[4][4];
        for (int row=0; row < 4; ++row) {
            for (int col=0; col < 4; ++col) {
                cin >> M2[row][col];
            }
        }

        for (int i=0; i<4; ++i) {
            s1.insert(M1[ans1-1][i]);
            s2.insert(M2[ans2-1][i]);
        }

        set<int> result;
        std::set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(), std::insert_iterator< set<int> >(result, result.begin()));



        cout << "Case #" << t+1 << ": ";
        if (result.size() == 1)
            cout << *result.begin();
        else if (result.size() > 1)
            cout << "Bad magician!";
        else
            cout << "Volunteer cheated!";
        cout << endl;

    }
}
