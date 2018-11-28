#include <iostream>
#include <cstdio>
#include <vector>
#include <map>

#define LARGE

using namespace std;

void populateDigits(map<int, int> &hmap, int n) {
    int r;
    int q = n;
    while(q != 0) {
        r = q % 10;
        q = q / 10;
        hmap[r] = 1;
    }
}


bool check(map<int, int> hmap) {
    for (int i = 0; i < 10; i++) {
        if (hmap.find(i) == hmap.end()) {
            return false;
        }
    }
    return true;
}

int process(int N) {
    if (N == 0) {
        return -1;
    }
    int lastNum = N;
    map<int, int> hmap;
    
    for (int j = 1; ;j++) {
        int n = N * j;
        populateDigits(hmap, n);
        if (check(hmap)) {
            return n;
        }
    }
}




int main() {
#ifdef SMALL
    freopen("A-small-practice.in", "rt", stdin);
    freopen("A-small-practice.out", "wt", stdout);
#endif
#ifdef LARGE
    freopen("A-large-practice.in", "rt", stdin);
    freopen("A-large-practice.out", "wt", stdout);
#endif
    
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N;
        cin >> N;
        int n = process(N);
        if ( n != -1) {
            cout << "Case #" << i + 1 << ": " << n << endl;
        } else {
            cout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
        }
    }
}