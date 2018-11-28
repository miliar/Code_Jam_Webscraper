#include<bits/stdc++.h>

using namespace std;

#define mp(x,y) make_pair(x, y)
#define For(i, n) for (int i = 0; i < (int) n; i++)

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

int main () {
    int T;
    cin >> T;
    For(cases, T) {
        string s; int m;
        cin >> s >> m;
        int count = 0;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '-') {
                if (i + m > s.size()) {
                    count = -1;
                    break;
                }
                for (int j = i; j < i + m; j++) {
                    s[j] = (s[j] == '-')?'+':'-';
                }
                count ++;
            }
        }
        printf("Case #%d: ", cases + 1);
        if (count == -1) printf("IMPOSSIBLE\n");
        else printf("%d\n", count);
    }
}
