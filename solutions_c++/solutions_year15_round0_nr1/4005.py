#include <string>
#include <cstdlib>
#include <iostream>
using namespace std;


char shy[1010];
int TC, N;


int main() {
    cin >> TC;
    for (int tc = 1; tc <= TC; tc++) {

        cin >> N >> shy;
        int res = 0, upsofar = (shy[0]-'0');
        for (int s = 1; s <= N; s++) {
            /* cout << upsofar << ' ' << res << endl; //DEB */
            if (shy[s]-'0' && upsofar < s) {
                res += s - upsofar;
                upsofar += s - upsofar;
            }
            upsofar += shy[s]-'0';
        }

        cout << "Case #" << tc << ": " << res << endl;

    }
    return 0;
}
