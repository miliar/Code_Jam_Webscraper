#define OSW2

#include <sstream>
#include <iostream>
#include <functional>
#include <algorithm>
#include <utility>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>

using namespace std;

typedef long long ll;


int main() {
#ifdef OSW
    freopen("//Users//osw//Desktop//in.txt", "r", stdin);
#endif
#ifdef OSW2
    string file_name = "C-small-attempt2";
    freopen(("//Users//osw//Downloads//" + file_name + ".in").c_str(), "r", stdin);
    freopen(("//Users//osw//Downloads//" + file_name + ".out").c_str(), "w", stdout);
#endif
    
    int T, t = 0;
    cin >> T;

    while (T-(t++)) {
        int n; cin >> n;

        vector<string> s[22];
        getchar();
        for (int i = 0; i < n; ++i) {
            string str;
            char ch;
            while ((ch=getchar())!='\n') {
                if (ch==' ') {
                    s[i].push_back(str);
                    //cout << str << ' ';
                    str = "";
                }
                else str += ch;
            }
            s[i].push_back(str);
            //cout << str << ' ';
            //cout << endl;
        }

        int ans = s[0].size()+s[1].size();

        for (int i = 0; i < n; ++i)
        {
         //   for(auto x:s[i]) cout << x << ' '; cout << endl;
        }

        for (int m=0; m<(1<<(n-2)); ++m) {
            auto E = s[0];
            auto F = s[1];
            for (int i=2; i<n; ++i) {
                if (m&(1<<(i-2)) ) {
                    for (auto&str: s[i]) E.push_back(str);
                }
                else {
                    for (auto&str: s[i]) F.push_back(str);
                }
            }
            sort(E.begin(), E.end());
            E.erase(unique(E.begin(), E.end()), E.end());
            sort(F.begin(), F.end());
            F.erase(unique(F.begin(), F.end()), F.end());

            vector<string>v(E.size()+F.size());
            ans = min(ans, (int)(set_intersection(E.begin(), E.end(), F.begin(), F.end(), v.begin()) - v.begin()) );
            //cout << m << endl;
            //for(auto x:v) cout << x << ' '; cout << endl;
        }

        cout << "Case #" << t << ": ";
        
        cout << ans << endl;
    }
}



