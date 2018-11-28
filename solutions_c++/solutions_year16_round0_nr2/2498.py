#include <string>
#include <iostream>
#include <vector>
#include <map>
#include <queue>

using namespace std;

int main()
{
    int T; cin >> T;
    for (int cas = 1; cas <= T; ++cas)
    {
        string st; cin >> st;
        while (st.back() == '+')
            st.pop_back();

        int len = st.size();
        string goal = string(len, '+');
        string goal_ = string(len, '-');

        int num_flips = 0;

        if (len == 0 || st == goal)
            num_flips = 0;
        else if (st == goal_)
            num_flips = 1;
        else {

            queue<string> Q;
            Q.push(st);
            map<string, int> pancakes2flips;
            pancakes2flips[st] = 0;
            while (!Q.empty()) {
                auto front = Q.front();
                Q.pop();
                auto cur_flips = pancakes2flips[front];

                // Generate next state brute force
                int newl = len;
                while (front[newl-1] == '+')
                    newl--;
                bool found = false;
                for (int i = 0; i < newl; ++i) {
                    string next = front;
                    for (int j = i, s = 0; j >= 0; --j, ++s) {
                        next[j] = front[s] == '+'? '-' : '+';
                    }
                    if (next == goal) {
                        num_flips = cur_flips+1;
                        found = true;
                        break;
                    }
                    if (next == goal_) {
                        num_flips = cur_flips+2;
                        found = true;
                        break;
                    }
                    if (pancakes2flips.find(next) == pancakes2flips.end()) {
                        Q.push(next);
                        pancakes2flips[next] = cur_flips + 1;
#ifdef DEBUG
                        cout << front << " ===> " << next << "\n";
#endif
                    }
                }
                if (found)
                    break;
            }
        }
        cout << "Case #" << cas << ": " << num_flips << "\n";
    }

    return 0;
}
