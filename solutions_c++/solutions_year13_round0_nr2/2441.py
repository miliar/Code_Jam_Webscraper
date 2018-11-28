#include <iostream>
#include <string>
#include <cstring>
#include <fstream>
#include <complex>
#include <limits>
#include <list>
#include <stack>
#include <numeric>
#include <queue>
#include <algorithm>
#include <functional>
#include <stack>
#include <bitset>
#include <map>
#include <set>
#include <map>
#include <list>
#include <math.h>
#include <set>
#include <stdio.h>
#include <ctype.h>
#include <vector>
#include <sstream>

using namespace std;


vector<string> getLineFields(istream& stream) {
    string line;
    getline(stream, line);
    stringstream str;
    str << line;
    vector<string> fields;
    string temp;
    while(str>>temp)
    {
        fields.push_back(temp);
    }
    return fields;
}

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        int m, n;
        cin >> m >> n;
        vector<vector<int> > l(m, vector<int>(n));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                cin >> l[i][j];
            }
        }
        
        vector<int> rows(m, 0);
        vector<int> cols(n, 0);
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                rows[i] = max(rows[i], l[i][j]);
                cols[j] = max(cols[j], l[i][j]);
            }
        }
        
        bool fail = false;
        for (int i = 0; i < m && !fail; ++i) {
            for (int j = 0; j < n && !fail; ++j) {
                if (l[i][j] < rows[i] && l[i][j] < cols[j]) {
                    fail = true;
                }
            }
        }

        if (!fail)
            cout << "Case #" << t + 1 << ": YES" << endl;
        else
            cout << "Case #" << t + 1 << ": NO" << endl;
    }
}
