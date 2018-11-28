#include <algorithm>
#include <iostream>
#include <set>
#include <vector>
using namespace std;

int main ()
{
    int cases; cin >> cases;

    for (int C = 1; C <= cases; ++C)
    {
        int f[16], fr, s[16], sr;
        cin >> fr;
        for (int i = 0; i < 16; ++i) cin >> f[i];
        cin >> sr;
        for (int i = 0; i < 16; ++i) cin >> s[i];

        // Fancy O(n log n) solution which takes 12.91 microseconds
        // ------------
        // set<int> fc, sc;
        // vector<int> c;
        // copy(&f[4*fr-4], &f[4*fr], inserter(fc, fc.begin()));
        // copy(&s[4*sr-4], &s[4*sr], inserter(sc, fc.begin()));
        // set_intersection(fc.begin(), fc.end(), sc.begin(), sc.end(), back_inserter(c));
        // printf("Case #%d: ", C);
        // if      (c.size() == 0) cout << "Volunteer cheated!";
        // else if (c.size() == 1) cout << c[0];
        // else                    cout << "Bad magician!";
        // cout << endl;
        // ------------

        // Unfancy O(n^2) solution which takes .19 microseconds
        // ------------
        int card = 0, count = 0;
        for (int i = 4*fr-4; i < 4*fr; ++i)
        {
            for (int j = 4*sr-4; j < 4*sr; ++j)
            {
                if (f[i] == s[j])
                {
                    card = f[i];
                    ++count;
                }
            }
        }
        printf("Case #%d: ", C);
        if      (count == 0) cout << "Volunteer cheated!";
        else if (count == 1) cout << card;
        else                 cout << "Bad magician!";
        cout << endl;
        // ------------
    }

    return 0;
}