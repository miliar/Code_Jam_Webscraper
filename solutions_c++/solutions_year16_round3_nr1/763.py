#include <iostream>
#include <vector>

using namespace std;

#define sz(v) (static_cast<int>((v).size()))

const int N = 200500;

int n;
vector<int> c[N];
                                        
void evac(string& s, int cnt) {
    int i = c[cnt].back();
    c[cnt].pop_back();
    s.push_back('a' + i);
    c[cnt - 1].push_back(i);
}

int main() {

    int tests;
    cin >> tests;

    for (int test = 0; test < tests; ++test) {
        cin >> n;
        for (int i = 0; i < n; ++i) {
            int idx;
            cin >> idx;
            c[idx].push_back(i);
        }

        vector<string> ans;

        for (int x = N - 2; x >= 1; --x) {
            while (sz(c[x]) > 0) {
                if (sz(c[x]) != 3 && sz(c[x]) != 1) {
                    string s;
                    evac(s, x);
                    evac(s, x);
                    ans.push_back(s);
                } else {
                    string s;
                    evac(s, x);
                    ans.push_back(s);
                }    
            }
        }

        cout << "Case #" << test + 1 << ":";
        for (int i = 0; i < sz(ans); ++i)
            cout << " " << ans[i];
        cout << endl;


    }



    return 0;
}