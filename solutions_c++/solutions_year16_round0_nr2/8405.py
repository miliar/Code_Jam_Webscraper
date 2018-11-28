# include <bits/stdc++.h>

# define fname "stones"
# define mp make_pair
# define F first
# define S second
# define y1 dsfkaj
# define pb push_back
# define prev adskjfa
typedef long long ll;

using namespace std;

string s;

int calc(int i) {
    if(i == -1)
        return 0;
    if(s[i] != s[i + 1])
        return calc(i - 1) + 1;
    else
        return calc(i - 1);
}

int main() {
    # ifdef alibi
        freopen("B-large.in", "r", stdin);
        freopen("output.txt", "w", stdout);
    # endif

    int T; cin >> T;
    for(int t = 1; t <= T; t++) {
        printf("Case #%d: ", t);
        cin >> s;
        s.push_back('+');
        cout << calc(s.size() - 2) << endl;
    }
    return 0;
}
