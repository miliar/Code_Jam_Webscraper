#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

#define endl '\n'

int main(int argc, char* argv[])
{
    cin.tie(0);
    ios::sync_with_stdio(false);

    int T, n;
    cin >> T;
    for (int t = 0; t < T; ++t)
    {
        cin >> n;
        vector<int> a;
        map<int,int> q;
        int temp;
        for (int j = 0; j < 2*n-1; ++j)
        {
            for (int k = 0; k < n; ++k)
            {
                cin >> temp;
                a.push_back(temp);
            }
        }
        sort(a.begin(), a.end());
        for (auto k = a.begin(); k != a.end(); ++k) q[*k] += 1;
        a.clear();
        for (auto k = q.begin(); k != q.end(); ++k)
        {
            if ((*k).second%2 == 1) a.push_back((*k).first);
        }
        sort(a.begin(), a.end());
        cout << "Case #" << t+1 << ": ";
        for (auto k = a.begin(); k != a.end(); ++k) cout << (*k) << " ";
        cout << endl;
    }

    return 0;
}

