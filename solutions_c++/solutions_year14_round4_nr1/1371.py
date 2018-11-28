#include <cstdio>
#include <iostream>
#include <map>

using namespace std;

void remove(map<int, int>& mm, int x) {
    mm[x]--;
    if (mm[x] == 0) {
        mm.erase(x);
    }
}

int main() {
    int T; cin >> T;

    for (int t = 0; t < T; ++t) {
        int N, X; cin >> N >> X;
        map<int, int> mm;

        for (int _n = 0; _n < N; ++_n) {
            int x; cin >> x;
            if (mm.find(x) == mm.end()) {
                mm[x] = 0;
            }
            mm[x]++;
        }

        int ans = 0;
        while (mm.size() != 0) {
            //cout << mm.size() << endl;
            //for (map<int,int>::iterator it = mm.begin(); it != mm.end(); it++)
            //    cout << it->first << " " << it->second << endl;

            int largest = mm.rbegin()->first;
            remove(mm, largest);

            int remain = X - largest;
            if (mm.size() > 0 && mm.begin()->first <= remain) {
                map<int,int>::iterator another_i = mm.upper_bound(remain);
                another_i--;
                int another = another_i->first;
                remove(mm, another);
            }

            ans++;
        }

        printf("Case #%d: %d\n", t+1, ans);
    }
}
