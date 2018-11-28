#include <iostream>
#include <fstream>

using namespace std;

ifstream fin ("A.in");
ofstream fout ("A.out");

int main()
{
    int T; fin >> T;
    for (int test = 1; test <= T; test++)
    {
        int x;
        string s;
        fin >> x >> s;
        
        int ans = 0, ctot = 0;
        for (int i = 0; i <= x; i++)
        {
            ans = max (ans, i - ctot);
            ctot += (s[i] - '0');
        }
        fout << "Case #" << test << ": " << ans << "\n";
    }
    return 0;
}
