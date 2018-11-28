#include <iostream>
#include <set>
using namespace std;

int main(int argc, char **argv) {
    int T = 0;
    cin >> T;
    std::set<int> collection;
    for (int i = 1; i <= T; i++) {
        int n = 0;
        cin >> n;
        if (n == 0) {
            cout << "Case #" << i << ": INSOMNIA" << endl;
            continue;
        }
        collection.clear();
        for (int j = n; ; j += n) {
            int tmp = j;
            while (tmp) {
                collection.insert(tmp % 10);
                tmp /= 10;
            }
            if (collection.size() == 10) {
                cout << "Case #" << i << ": " << j << endl;
                break;
            }
        }
    }
    return 0;
}
