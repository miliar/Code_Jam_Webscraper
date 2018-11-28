#define OSW2

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
    string file_name = "A-large";
    freopen(("//Users//osw//Desktop//" + file_name + ".in").c_str(), "r", stdin);
    freopen(("//Users//osw//Desktop//" + file_name + ".out").c_str(), "w", stdout);
#endif
    
    int T, t = 0;
    cin >> T;

    while (T-(t++)) {
        int M;
        char ch[1001];
        int cnt = 0;
        int ans = 0;
        cin >> M;
        for (int i = 0; i <= M; ++i) {
        	cin >> ch[i];
        	if (cnt < i) {
        		ans += i-cnt;
        		cnt = i;
        	}
        	cnt += ch[i]-'0';
        }

        cout << "Case #" << t << ": ";
        cout << ans << endl;

    }
}



