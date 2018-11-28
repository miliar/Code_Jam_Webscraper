#include <iostream>
#include <vector>
using namespace std;

bool check(const int x, const int y, vector<string>& lawn) {
    bool check_x = true, check_y = true;
    for(unsigned int i = 0; check_x && i < lawn[0].length(); ++i) {
        if(lawn[y][x] < lawn[y][i]) check_x = false;
    }
    for(unsigned int i = 0; check_y && i < lawn.size(); ++i) {
        if(lawn[y][x] < lawn[i][x]) check_y = false;
    }
    return check_x || check_y;
}

int main(void) {
    int t;
    cin >> t;

    for(int case_n = 1; case_n <= t; ++case_n) {
        int n, m;
        cin >> n >> m;

        vector<string> lawn(n);
        for(int y = 0; y < n; ++y) {
            string str;
            for(int x = 0; x < m; ++x) {
                string tmp;
                cin >> tmp;
                str += tmp;
            }
            lawn[y] = str;
        }

        bool ok = true;
        for(int y = 0; ok && y < n; ++y) {
            for(int x = 0; ok && x < m; ++x) {
                if(!check(x, y, lawn)) ok = false;
            }
        }

        cout << "Case #" << case_n << ": ";
        if(ok) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
    return 0;
}
