#include <iostream>
#include <fstream>
#include <unordered_map>
#include <cstring>

using namespace std;

int N;

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    fin >> N;
    char s[110];
    fin.getline(s, 110);
    for (int i = 0; i < N; ++ i)
    {
        fin.getline(s, 110);
        int ls = strlen(s);
        char ns[110];
        int lns = 0;
        for (int j = 0; j < ls; ++ j)
        {
            if (lns == 0 || s[j] != ns[lns - 1])
            {
                ns[lns ++] = s[j];
            }
        }
        int ans = 0;
        if (ns[0] == '+')
        {
            ans = lns / 2 * 2;
        }
        else
        {
            ans = 1 + (lns - 1) / 2 * 2;
        }
        fout << "Case #" << i + 1 << ": ";
        fout << ans;
        fout << endl;
    }
    return 0;
}

