#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <string>
#include <string.h>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <cstring>
#include <queue>
#include <bitset>
#include <queue>
#include <map>


using namespace std;


int p[1001];


int main() {
    freopen("twopaths.in", "r", stdin);
    freopen("twopaths.out", "w", stdout);
    int t;
    cin >> t;
    for (int ii = 0; ii < t; ii++) {
        int n;
        cin >> n;
        int sum = 0;
        set<pair<int, int> > s;
        for (int i = 0; i < n; i++) {
            cin >> p[i];
            sum += p[i];
            s.insert(make_pair(p[i], i));
        }
        cout << "Case #" << ii + 1 << ':' << ' ';
        while (sum != 0) {
            set<pair<int, int> >::reverse_iterator it = s.rbegin();
            pair<int, int> h = *it;
            it++;
            pair<int, int> h1 = *it;
            //cout << h.second << ' ' << h1.second << endl;
            if (h.first == 1) {
                if (sum == 2) {
                    cout << char('A' + h.second) << char('A' + h1.second) << ' ';
                    sum -= 2;
                } else {
                    cout << char('A' + h.second) << ' ';
                    sum--;
                    s.erase(h);
                    s.insert(make_pair(h.first - 1, h.second));
                }
                continue; 
            }     
            if (h1.first <= (sum - 2) / 2) {
                cout << char('A' + h.second) << char('A' + h.second) << ' ';
                s.erase(h);
                h.first -= 2;
                sum -= 2;
                if (h.first != 0) {
                    s.insert(h);
                }
                continue;
            }
            if (h1.first <= (sum - 1) / 2) {
                cout << char('A' + h.second) << ' ';
                s.erase(h);
                h.first -= 1;
                sum -= 1;
                if (h.first != 0) {
                    s.insert(h);
                }
                continue;
            }
            cout << char('A' + h.second) << char('A' + h1.second) << ' ';
            s.erase(h);
            s.erase(h1);
            h.first -= 1;
            h1.first -= 1;
            sum -= 2;
            if (h.first != 0) {
                s.insert(h);
            }
            if (h1.first != 0) {
                s.insert(h1);
            }
        }
        cout << endl;
    }
    return 0;
}
