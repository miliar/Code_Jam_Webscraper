#include <bits/stdc++.h>

using namespace std;

int main(int argc,char *argv[])
{
    int T;
    cin >> T;
    for (int t=0;t<T;t++)
    {
        int K,C,S;
        cin >> K >> C >> S;
        cout << "Case #" << t+1 << ":";
        long long step = 1;
        for (int i=1;i<C;i++)
            step *= (long long)K;
        step += step/(long long)K;

        long long KC = 1;
        for (int i=0;i<C;i++)
            KC *= (long long)K;

        long long v = 1;
        if (v+step*S<KC)
        {
            cout << " IMPOSSIBLE" << endl;
        } else
        {
            for (int i=0;i<S;i++)
            {
                cout << " " << v;
                v += step;
            }
            cout << endl;
        }
    }
    return 0;
}
