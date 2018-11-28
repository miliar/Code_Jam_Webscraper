#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define mt make_tuple
#define ll long long
#define pii pair<int,int>
#define tii tuple <int,int,int>
#define N 200005
#define mod 1000000005
#define X first
#define Y second
#define eps 0.0000000001
#define all(x) x.begin(),x.end()
#define tot(x) x+1,x+n+1
using namespace std;

int t, T, n, i;
char s[1010];
deque<char>sol;

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    scanf("%d", &T);

    for(t = 1; t <= T; t++) {
        printf("Case #%d: ", t);
        scanf("%s", &s);
        n = strlen(s);
        sol.resize(0);

        for(i = 0; i < n; i++) {
            if(s[i] >= sol[0])
                sol.push_front(s[i]);
            else
                sol.pb(s[i]);
        }

        for(auto it : sol)
            printf("%c", it);

        printf("\n");
    }

    return 0;
}
