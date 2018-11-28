#include <iostream>
#include <cstdio>
#include <bitset>
#include <queue>
#include <string>
#include <unordered_set>
using namespace std;

bool happy(bitset<110> &pancakes, int size) {
    for (int i = 0; i < size; i++) {
        if (!pancakes.test(i))
            return false;
    }

    return true;
}

bitset<110> flip(bitset<110> &pancakes, int n) {
    bitset<110> p = pancakes;
    for (int i = 0; i < n; i++) {
        p.flip(i);
    }

    return p;
}

int main() {
    int N;
    cin >> N;

    for (int i = 1; i <= N; i++) {
        bitset<110> pancakes;
        string ss;

        cin >> ws;
        printf("Case #%d: " , i);

        getline(cin, ss);

        int size = ss.size();
        for (int j = 0; j < size; j++) {
            pancakes[j] = (ss[j] == '+' ? 1 : 0);
        }

        int count = 0;
        int j = size - 1;
        while (!happy(pancakes, size)) {
            if (!pancakes.test(j)) {
                pancakes = flip(pancakes, j + 1);
                count++;
            }
            j--;
        }

        cout << count << endl;
    }

    return 0;
}
