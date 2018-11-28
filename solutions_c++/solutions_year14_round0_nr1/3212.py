#include <iostream>
#include <set>
#include <algorithm>
#include <iterator>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    int T;
    cin >> T;
    for(int t=1; t<=T; ++t) {
        cout << "Case #" << t << ": ";
        int a[2];
        int cards[2][4][4];
        for(int i=0; i<2; ++i) {
            cin >> a[i];
            for(int y=0; y<4; ++y) for(int x=0; x<4; ++x)
                cin >> cards[i][y][x];
        }
        set<int> possible[2];
        set<int> res;
        for(int i=0; i<2; ++i) for(int x=0; x<4; ++x)
            possible[i].insert(cards[i][a[i]-1][x]);
        set_intersection(begin(possible[0]),end(possible[0]),begin(possible[1]),end(possible[1]),inserter(res,begin(res)));
        switch(res.size()) {
            case 1:
                cout << *begin(res);
                break;
            case 0:
                cout << "Volunteer cheated!";
                break;
            default:
                cout << "Bad magician!";
        }
        cout << endl;
    }
}
