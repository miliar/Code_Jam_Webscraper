#include<iostream>
#include<string>
#include<bitset>
#define HAPPY '+'
#define SAD '-'

using namespace std;


int solve(string s, int k) {
    bitset<1000> pancake;
    swap(s.begin(), s.end());
    for (int i = 0; i < s.size(); ++i) if (s[i] == HAPPY) pancake.set(i);
    //cerr << pancake << endl;
    int flips = 0;
    int i;
    for (i = 0; i < s.size() - k + 1; ++i) {
        if (!pancake[i]) {
            flips++;            
            for (int j = 0; j < k; ++j) {
                pancake[i+j].flip();
            }
            //cerr << "Flipping " << i << " " << pancake << endl;
        }
    }
    for (; i < s.size(); ++i) {
        if (!pancake[i]) {
            return -1;
        }
    }

    return flips;
}

int main() {
    int t, k;
    string s;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cin >> s >> k;
        int solution = solve(s, k);
        cout << "Case #" << i << ": ";
        if (solution == -1) {
            cout << "IMPOSSIBLE" << endl;
        }
        else {
            cout << solution << endl;
        }
    }
    return 0;
}
