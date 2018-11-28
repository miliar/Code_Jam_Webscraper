#include <iostream>
#include <cmath>
#include <set>
using namespace std;
inline int min(int a, int b) { return a < b ? a : b; }
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int tc;
    cin >> tc;
    for (int a = 0; a < tc; ++a) {
        int num, inp, mini, cnt = 0;
        multiset<int> st;
        cin >> num;
        while(num--) {
            cin >> inp;
            st.insert(inp);
        }
        mini = *--st.end();
        while(*--st.end() >= 4) {
            int end = *--st.end();
            st.erase(--st.end());
            if (end == 9) {
                bool hassix = false; bool allbelowthree = true;
                for (set<int>::iterator it = st.begin(); it != st.end(); ++it) {
                    hassix |= *it == 6;
                    allbelowthree &= *it <= 3;
                }
                if (hassix || allbelowthree) {
                    st.insert(3);
                    st.insert(6);
                } else {
                    st.insert(4);
                    st.insert(5);
                }
            } else {
                st.insert((ceil)((double)end / 2));
                st.insert((floor)((double)end / 2));
            }
            ++cnt;
            mini = min(mini, cnt + *--st.end());
        }
        cout << "Case #" << a + 1 << ": " << mini << "\n";
    }
    return 0;
}