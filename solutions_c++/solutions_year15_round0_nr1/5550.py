#include <iostream>
#include <cstdio>
#include <cstring>
#include <fstream>
#include <algorithm>

using namespace std;

int main () {
    freopen ("A-large.in","r",stdin);
    freopen ("A-large.out","w",stdout);

    int t;
    cin >> t;

    for (int a = 1; a <= t; a++) {
        int high;
        cin >> high;
        string s;
        cin >> s;

        //cout << t << endl;

        int stand = 0;
        int need = 0;

        //cout <<high << endl;

        for (int i = 0;i <= high; i++) {
            if (stand < i) {
                need += i - stand;
                stand = i;
            }

            stand += s.at(i) - '0';


        }

        cout << "Case #" << a << ": " << need << endl;
    }



    return 0;
}
