#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    freopen("input.txt", "r",stdin);
    freopen("output.txt", "w",stdout);
    int T;
    cin >> T;
    for (int z = 0; z < T; ++z)
    {
        int fr = 0;
        int sum = 0;
        int m;
        cin >> m;
        string S;
        cin >> S;
        for (int i = 0; i <= m; ++i)
        {
            char c = S[i];
            int a = c - '0';
            if (i > sum)
            {
                fr += i - sum;
                sum += i - sum;
            }
            sum += a;
        }
        cout << "Case #" << z + 1 << ": " << fr << endl;
    }
    return 0;
}
