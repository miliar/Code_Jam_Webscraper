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
        int K;
        fin >> K >> K >> K;
        
        fout << "Case #" << t << ":";
        
        for (int i = 0; i < K; i++)
            fout << " " << i + 1;
        fout << "\n";
    }
    return 0;
}
