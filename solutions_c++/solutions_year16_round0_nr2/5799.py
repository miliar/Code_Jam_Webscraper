#include <iostream>
#include <string>
#include <stack>

using namespace std;

int solve(string str) {
    stack<bool> st, st_tmp;
    int cnt = 0;
    int downSide = 0;
    int lastDown = 0;
    for (int i = str.length() - 1; i >= 0; --i) {
        if(str.at(i) == '+') {
            st.push(1);
        } else {
            st.push(0);
            ++downSide;
            if(lastDown == 0) {
                lastDown = i + 1;
            }
        }
    }
    while(downSide) {
        cnt++;
        while(lastDown--) {
            st_tmp.push(st.top());
            st.pop();
        }
        while(!st_tmp.empty()) {
            if(st_tmp.top()) {
                downSide++;
                if(lastDown == -1) {
                    lastDown = st_tmp.size();
                }
            } else {
                downSide--;
            }
            st.push(!st_tmp.top());
            st_tmp.pop();
        }
    }
    return cnt;
}

int main(int argc, char *argv[]) {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        string str;
        cin >> str;
        cout << "Case #" << i + 1 << ": ";
        cout << solve(str) << endl;
    }
    return 0;
}
