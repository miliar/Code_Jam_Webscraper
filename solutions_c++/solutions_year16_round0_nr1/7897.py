#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <utility>
#include <climits>
#include <unordered_set>
#include <set>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        long long n, current = 0;
        cin >> n;
        if (n == 0) {
            cout << "Case #" << t << ": INSOMNIA" << endl;
        } else {
            unordered_set<int> num;
            while (num.size() < 10) {
                current += n;
                long long temp = current;
                while (temp) {
                    num.insert(temp%10);
                    temp /= 10;
                }
            }
            cout << "Case #" << t << ": " << current << endl;
        }
    }
    return 0;
}

