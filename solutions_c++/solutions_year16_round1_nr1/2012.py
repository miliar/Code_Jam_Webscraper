#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
 
using namespace std;
 
int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    int T;
    fin >> T;
     
    string S;
    for (int t = 1 ; t <= T; t++)
    {  
        fin >> S;
        string ans;
        ans = S[0];
        for (int i = 1 ; i < S.size() ; i++) {
            if (S[i] >= ans[0]) 
                ans = S[i] + ans;
            else 
                ans = ans + S[i];
        }

        fout << "Case #" << t << ": " << ans << endl;
    }
}
