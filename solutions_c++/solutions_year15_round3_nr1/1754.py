#include <algorithm>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <climits>
#include <numeric>

using namespace std;

int main() {
    string name = "A-small";
    string path = "/Users/cpdehli/Desktop/Google/q1/";
    
    
    freopen((path + name + ".in").c_str(), "r", stdin);
    freopen((path + name + ".out").c_str(), "w", stdout);

    int test_cases;
    cin >> test_cases;
    
    for (int test_case = 1; test_case <= test_cases; test_case++) {
        float R, C, W;
        cin >> R;
        cin >> C;
        cin >> W;
        
        int total = R * ceil(C / W) + (W - 1);
        
        cout << "Case #" << test_case << ": " << total << endl;
        cout.flush();
    }
    
    fclose(stdout);
    fclose(stdin);
    return 0;
}
