#include <iostream>
#include <fstream>

using namespace std;

ifstream fin ("D.in");
ofstream fout ("D.out");

string res = "1111" "1111" "1111" "1111" 
             "0101" "1111" "0101" "1111" 
             "0000" "0010" "0111" "0010" 
             "0000" "0000" "0001" "0011";

int main()
{
    int T; fin >> T;
    for (int test = 1; test <= T; test++)
    {
        int x, r, c;
        fin >> x >> r >> c;
        x--, r--, c--;
        int val = 16 * x + 4 * r + c;
        fout << "Case #" << test << ": " << ((res[val] == '0') ? "RICHARD" : "GABRIEL") << "\n";
    }
    return 0;
}
