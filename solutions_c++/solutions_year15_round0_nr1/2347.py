#include <iostream>
#include <cstdio>

using namespace std;

int main()
{

    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int T;
    cin >> T;
    for (int test = 0; test < T; test++) {
        int N;
        cin >> N;
        string s;
        cin >> s;
        int result = 0;
        int current = 0;
        for (int i = 0; i <= N; i++) {
            if (s[i] == '0')
                continue;
            if (current < i) {
                result += i - current;
                current = i;
            }
            current += s[i] - '0';
        }
        cout << "Case #" << test + 1 << ": " << result << endl;
    }
    return 0;
}

