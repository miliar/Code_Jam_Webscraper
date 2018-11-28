#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    int t, K, C, S;
    cin >> t;
    for(int c = 1;c <= t;++c)
    {
        cin >> K >> C >> S;
        cout << "Case #" << c << ":";
        for(int i = 1;i <= K;++i)
            cout << ' ' << i;
        cout << endl;
    }
    return 0;
}
