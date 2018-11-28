#include <fstream>
#include <algorithm>
#include <set>

using namespace std;

int main() {
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    int testCount;
    cin >> testCount;
    for (int test = 1; test <= testCount; ++test) {
        int n, capacity;
        cin >> n >> capacity;
        multiset<int> sizes;
        for (; n > 0; --n) {
            int size;
            cin >> size;
            sizes.insert(size);
        }
        int answer = 0;
        while (!sizes.empty()) {
            ++answer;
            int now1 = *sizes.rbegin();
            sizes.erase(sizes.find(now1));
            multiset<int>::iterator now2 = sizes.upper_bound(capacity - now1);
            if (now2 != sizes.begin())
                sizes.erase(--now2);
        }
        cout << "Test #" << test << ": " << answer << "\n";
    }
    cin.close();
    cout.close();
    return 0;
}
