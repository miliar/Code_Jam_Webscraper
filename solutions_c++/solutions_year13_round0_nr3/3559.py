#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>

using namespace std;

bool ispal(int i) {
    ostringstream ss;
    ss << i;
    string s = ss.str();
    return equal(s.begin(), s.end(), s.rbegin());
}

void solve() {
    int min, max;
    cin >> min >> max;
    min = ceil(sqrt(min));
    max = floor(sqrt(max));
    
    int pal = 0;
    for (int i=min; i<=max; i++)
        if (ispal(i) && ispal (i*i)) pal++;
    cout << pal;
}


int main(int argc, char** argv) {
    int tmax;
    cin >> tmax;
    
    for (int t=1; t<=tmax; t++) {
        
        cout << "Case #" << t << ": ";
        solve();
        cout << endl;
    }
}
