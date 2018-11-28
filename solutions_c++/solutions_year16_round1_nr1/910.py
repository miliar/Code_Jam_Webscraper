#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

string s;
list <char> l;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int nTests = 0;
    scanf("%d", &nTests);
    for(int Case = 1; Case <= nTests; ++Case) {
        cin >> s;
        l.clear();
        l.push_back(s[0]);
        for(int i = 1; i < (int)s.size(); ++i)
            if (s[i] >= l.front()) l.push_front(s[i]);
            else l.push_back(s[i]);

        printf("Case #%d: ", Case);
        for(list <char> :: iterator it = l.begin(); it != l.end(); ++it)
            printf("%c", *it);
        printf("\n");
    }

    return 0;
}
