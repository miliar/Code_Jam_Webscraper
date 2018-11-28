#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream fin ("A.in");
ofstream fout ("A.txt");

int main()
{
    int T; fin >> T;
    for (int t = 1; t <= T; t++)
    {
        string S; fin >> S;
        
        bool x[10];
        for (int i = 0; i < 10; i++)
            x[i] = false;
        
        fout << "Case #" << t << ": ";
        
        int ans = 0;
        if (S[S.length()-1] == '-')
            ans++;
        for (int i = 0; i < S.length() - 1; i++)
            if (S[i] != S[i+1])
                ans++;
        fout << ans << "\n";
    }
    return 0;
}
