
#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
using namespace std;

#define rep(i,n) for (int i = 0; i < int(n); i++)
#define all(c) (c).begin(), (c).end()

int T,i,j,a[4][4],b[4][4];

int main() {
    cin >> T;
    rep (t,T) {
        cout << "Case #" << t+1 << ": ";
        cin >> i;
        rep (p,4) rep (q,4) cin >> a[p][q];
        cin >> j;
        rep (p,4) rep (q,4) cin >> b[p][q];

        set<int> A, B;
        vector<int> I;
        rep (q,4) A.insert(a[i-1][q]), B.insert(b[j-1][q]);
        set_intersection(all(A), all(B), back_inserter(I));
        if (I.size() == 1) {
            cout << *I.begin() << endl;
        } else if (I.size() > 1) {
            cout << "Bad magician!" << endl;
        } else {
            cout << "Volunteer cheated!" << endl;
        }
    }
}
