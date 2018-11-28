#include <fstream>
#include <set>

using namespace std;

const int MAXN = 10 * 1000 + 5;
set< pair<int, int> > st;

int main() {
    ifstream in("input.txt");
    ofstream out("output.txt");
    int t;
    in >> t;
    for(int tt = 0; tt < t; tt++) {
        int n, x;
        in >> n >> x;
        for(int i = 0; i < n; i++) {
            int a;
            in >> a;
            st.insert(make_pair(a, i));
        }
        int ans = 0;
        while(!st.empty()) {
            int q = st.begin()->first;
            set< pair<int, int> >::iterator it = st.lower_bound(make_pair(x - q + 1, -1));
            if(it == st.begin()) {
                st.erase(it);
                ans++;
            }
            else {
                it--;
                if(it != st.begin())
                    st.erase(it);
                st.erase(st.begin());
                ans++;
            }
        }
        out << "Case #" << tt + 1 << ": " << ans << '\n';
    }
    return 0;
}
