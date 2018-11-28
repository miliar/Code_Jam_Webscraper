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

bool used[10];

int main() {
    # ifdef alibi
        freopen("A-large.in", "r", stdin);
        freopen("output.txt", "w", stdout);
    # endif

    int T; cin >> T;
    for(int t = 1; t <= T; t++) {
        int n; cin >> n;
        int cnt = 0;
        printf("Case #%d: ", t);
        for(int i = 1; i <= 100; i++) {
            int x = n * i;
            while(x) {
                cnt += (used[x % 10] ^ 1);
                used[x % 10] = true;
                x /= 10;
            }
            if(cnt == 10) {
                cout << i * n << endl;
                break;
            }
        }
        if(cnt != 10)
            puts("INSOMNIA");
        for(int i = 0; i <= 9; i++)
            used[i] = false;
    }
    return 0;
}
