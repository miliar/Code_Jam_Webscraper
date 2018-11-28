#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;

ifstream fin ("A.in");
ofstream fout ("A.out");

int arr[16], arr2[16];
int r1, r2;

int main()
{
    int ntest; fin >> ntest;
    for (int test = 0; test < ntest; test++)
    {
    
    fin >> r1;
    for (int i = 0; i < 16; i++)
    {
        int t; fin >> t;
        arr[t-1] = i / 4;
    }
    fin >> r2;
    for (int i = 0; i < 16; i++)
    {
        int t; fin >> t;
        arr2[t-1] = i / 4;
    }
    
    r1--, r2--;
    int ans = -1, num = 0;
    for (int i = 0; i < 16; i++)
        if (arr[i] == r1 && arr2[i] == r2)
        {
            ans = i + 1;
            num++;
        }
    
    fout << "Case #" << test + 1 << ": ";
    if (num == 0)
        fout << "Volunteer cheated!\n";
    else if (num == 1)
        fout << ans << "\n";
    else
        fout << "Bad magician!\n";
    }
    
    //system ("Pause");
    return 0;
}
