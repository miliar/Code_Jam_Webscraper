#include <iostream>
#include <fstream>
#include <cstdlib>
using namespace std;
int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    int T;
    fin >> T;
    for (int cc=1; cc<=T; cc++)
    {
        int n;
        int ans=0;
        char ch;
        fin >> n;
        fin >> ch;
        int sum = ch - '0';
        for (int i=1; i<=n; i++)
        {
            fin >> ch;
            if ( sum >= i) sum+= ch - '0';
                else {
                    ans += i - sum;
                    sum = i + ch - '0';
                }
        }
        fout << "Case #" << cc << ": " << ans <<endl;
    }
    return 0;
}
