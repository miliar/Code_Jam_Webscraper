#include <iostream>
#include <bitset>
#include <stdint.h>

using namespace std;

void check(bitset<10> &d, int64_t curr) {
    while(curr > 0) {
        d.set(curr % 10, true);
        curr /= 10;
    }
}

int64_t solve(int64_t n) {
    if(n == 0) return -1;
    bitset<10> d;
    int64_t curr = 0;
    while(!d.all()) {
        curr += n;
        check(d, curr);
    }
    return curr;
}

int main()
{
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        int64_t N;
        cin >> N;
        int64_t result = solve(N);
        cout << "Case #" << t << ": ";
        result == -1 ? cout << "INSOMNIA" : cout << result;
        cout << endl;
    }
    return 0;
}
