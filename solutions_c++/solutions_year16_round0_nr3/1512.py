#include <bits/stdc++.h>

typedef long long ll;
using namespace std;

int N, J;
int cnt;
void gen(string s, int atual, int q)
{
    if (cnt == J)
        return;
    if(atual == N && !q && s[N - 1] == '1')
    {
        cout << s << " ";
        for (int i = 3; i < 12; i++)
            cout << i << " ";
        cout << endl;
        cnt++;
        return;
    }
    else if (atual == N)
        return;

    int add;
    if (atual % 2) add = -1;
    else add = +1;
    gen(s + '1', atual + 1, q + add);
    if (cnt == J)
        return;
    gen(s + '0', atual + 1, q);
}
int main()
{
    int t;

    cin >> t;

    for (int i = 0; i < t; i++)
    {
        cnt = 0;
        cin >> N >> J;
        cout << "Case #" << i + 1 << ":" << endl;
        string s = "1";
        int q = 1;
        gen(s, 1, q);
    }
}
