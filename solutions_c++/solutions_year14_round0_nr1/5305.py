#include <vector>
#include <cmath>
#include <cstdio>
#include <list>
#include <cctype>
#include <cstring>
#include <iomanip>
#include <stack>
#include <map>
#include <iostream>
#include <string>
#include <sstream>
#include <set>

using namespace std;

void func() {
    int ans1, ans2;
    int f[17] = { 0 };

    string s;

    cin >> ans1;
    getline(cin, s);

    for (int i = 1; i <= ans1; ++i)
        getline(cin, s);

    stringstream ss(s);
    for (int i = 0; i < 4; ++i) {
        int t = 0;
        ss >> t;
        f[t] = 1;
    }

    for (int i = ans1+1; i <= 4; ++i)
        getline(cin, s);

    cin >> ans2;
    getline(cin, s);
    for (int i = 1; i <= ans2; ++i)
        getline(cin, s);

    stringstream ss2(s);
    int cnt = 0;
    int can = 0;
    for (int i = 0; i < 4; ++i) {
        int t = 0;
        ss2 >> t;
        if (f[t] != 0) {
            cnt++;
            can = t;
        }
    }

    for (int i = ans2+1; i <= 4; ++i)
        getline(cin, s);

    if (cnt == 1)
        cout << can << endl;
    else if (cnt > 1)
        cout << "Bad magician!" << endl;
    else if (cnt == 0)
        cout << "Volunteer cheated!" << endl;
}


//////////////////////////////

char in_file[] = "A-small-attempt1.in";
char out_file[] = "test.out";

int main() {
    int case_count, t;

    freopen(in_file, "r", stdin);
    freopen(out_file,"w", stdout);

    string s;
    cin >> case_count;
    getline(cin, s);
    for (t = 1; t <= case_count; t++) {
        cerr << "\nDealing Case #" << t << endl;
        cout << "Case #" << t << ": ";
        func();
    }

	return 0;    
}
