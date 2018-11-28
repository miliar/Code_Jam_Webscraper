#include <iostream>
#include <fstream>
#include <unordered_map>
#include <cstring>
#include <queue>

using namespace std;

int T, N, K;

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    fin >> T;
    for (int i = 0; i < T; ++ i)
    {
        char a[1001];
        fin >> a;
        string ans;
        ans += a[0];
        for (int j = 1; j < strlen(a); ++ j)
        {
            if (a[j] >= ans[0])
            {
                ans = a[j] + ans;
            }
            else
            {
                ans += a[j];
            }
        }
        fout << "Case #" << i + 1 << ": ";
        fout << ans;
        fout << endl;
    }
    return 0;
}


