#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <list>
#include <iterator>
#include <sstream>
#include <cmath>
#include <iomanip>
#include <cstdio>

using namespace std;

typedef vector<int> vi;
typedef vector<double> vd;

int main() {
    int T;
    cin >> T;
    for (int cs=1; cs<=T; ++cs) {
        int ans = 0;
        int Smax;
        cin >> Smax;
        vector<char> shc(Smax+1);
        for (int i=0; i<=Smax; ++i)
            cin >> shc[i];
        vector<int> sh;
        for (int i=0; i<=Smax; ++i) {
            int k = shc[i]-'0';
            for (int j=0; j<k; ++j)
                sh.push_back(i);
        }
        sort(sh.begin(), sh.end());
        // copy(sh.begin(), sh.end(), ostream_iterator<int>(cout, " ")); cout << endl;
        for (int i=0; i<=Smax; ++i) {
            if (sh[i]>(i+ans)) ans = sh[i] - i;
        }
        cout << "Case #" << cs << ": " << ans << "\n";
    }
}
