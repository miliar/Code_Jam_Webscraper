#include <bits/stdc++.h>
//#define LOCAL

using namespace std;

int main ()
{
    ios_base::sync_with_stdio(0);
#ifdef LOCAL
    ifstream cin ("D:\\in2.txt");
#else
    ifstream cin ("D:\\DOWNLOADS\\A-large.in");
    ofstream cout ("D:\\outA0-large.txt");
#endif

    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        int n, cap;
        cin >> n >> cap;
        vector <int> files (n);
        for (int j = 0; j < n; ++j)
            cin >> files[j];
        vector <char> used(n);
        int cnt = 0;
        std::sort (files.begin(), files.end(), greater <int> ());
        for (int j = 0; j < n; ++j)
        {
            if (used[j]) continue;
            for (int k = j + 1; k < n ; ++k)
            {
                if (used[k]) continue;
                if (files[j] + files[k] <= cap)
                {
                    used[j] = 1;
                    used[k] = 1;
                    break;
                }
            }
            ++cnt;
        }
        cout << "Case #" << i + 1 << ": " << cnt << endl;
    }
}
