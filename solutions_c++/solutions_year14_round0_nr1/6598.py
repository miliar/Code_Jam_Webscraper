#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cassert>
#include <string.h>
#include <sstream>
#include <fstream>


using namespace std;

#define ll unsigned long long

template<class T> string toString(T n){ostringstream ost;ost<<n;ost.flush();return ost.str();}//NOTES:toString(

const ll MOD = 1000000007;




int main() {

    int tt;

    ifstream cin("A-small-attempt0.in");
    ofstream cout("ans.txt");

    cin >> tt;
    int c = 1;

    while (tt--) {
        int n, m;
        int a[5][5], b[5][5];

        cin >> n;
        for (int i = 1; i <= 4; i++)
            for (int j = 1; j <= 4; j++)
                cin >> a[i][j];
        cin >> m;
        for (int i = 1; i <= 4; i++)
            for (int j = 1; j <= 4; j++)
                cin >> b[i][j];

        int t = 0, ans = 0;

        for (int i = 1; i <= 4; i++)
            for (int j = 1; j <= 4; j++)
                if (a[n][i] == b[m][j])
                {
                    t++;
                    ans = a[n][i];
                }

        cout << "Case #" << c++ << ": ";
        if (t > 1)cout << "Bad magician!" << endl;
        else if (t == 0)
            cout << "Volunteer cheated!" << endl;
        else cout << ans << endl;
    }

    return 0;
}
