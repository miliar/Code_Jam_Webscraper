#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int TT, head, tail;
    char s[1010];
    char ans[1010];

    cin >> TT;
    for (int T = 1; T <= TT; ++T)
    {
        cin >> s;
        head = 0;
        tail = 1;
        ans[0] = s[0];
        int l = strlen(s);
        for (int i = 1; i < l ; ++i)
            if (s[i] >= ans[head])
            {
                head = (head - 1 + 1005) % 1005;
                ans[head] = s[i];
            }
            else
            {
                ans[tail] = s[i];
                tail = (tail + 1) % 1005;
            }
        cout << "Case #" << T << ": ";
        for (int i = head; i != tail; i = (i+1)%1005)
            cout << ans[i];
        cout <<endl;
    }

    fclose(stdout);
    fclose(stdout);
    return 0;
}
