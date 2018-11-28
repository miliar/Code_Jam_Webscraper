#include <bits/stdc++.h>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        string buffer;
        cin >> buffer;

        deque<char> winning;
        for(size_t i = 0; i < buffer.size(); i++) {
            if(i == 0) winning.push_back(buffer[i]);
            else {
                if(buffer[i] >= winning.front()) {
                    winning.push_front(buffer[i]);
                } else {
                    winning.push_back(buffer[i]);
                }
            }

        }


        cout << "Case #" << t << ": ";
        for(auto &it : winning) {
            cout << it;
        }
        cout << endl;
    }

    return 0;
}
