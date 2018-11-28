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

const int MAXN = (int)5e5 + 5;


int main() {
    # ifdef alibi
        freopen("A-large (1).in", "r", stdin);
        freopen("output.txt", "w", stdout);
    # endif

    int T; cin >> T;
    for(int test = 1; test <= T; test++) {
        printf("Case #%d: ", test);
        string s; cin >> s;
        deque < char > ans;
        ans.push_back(s[0]);
        for(int i = 1; i < s.size(); i++)
            if(s[i] >= ans.front())
                ans.push_front(s[i]);
            else
                ans.push_back(s[i]);
        while(!ans.empty()) {
            putchar(ans.front());
            ans.pop_front();
        }
        puts("");
    }
    return 0;
}

