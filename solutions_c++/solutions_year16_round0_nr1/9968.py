#include <iostream>
#include <set>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);

    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {
        long long n;
        cin >> n;

        if (n == 0) {
            cout << "Case #" << (i + 1) << ": INSOMNIA" << endl;
            continue;
        }

        set<int> st;
        long long curNum = n;
        bool found = false;

        for (int z = 0; z < 1000; z++) {
            long long numCopy = curNum;
            while (numCopy) {
                st.insert(numCopy % 10);
                numCopy /= 10;
            }

            if (st.size() == 10) {
                found = true;
                break;
            }

            curNum += n;
        }

        if (found)
            cout << "Case #" << (i + 1) << ": " << curNum << endl;
        else
            cout << "Case #" << (i + 1) << ": INSOMNIA" << endl;
    }

    return 0;
}