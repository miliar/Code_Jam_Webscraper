#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;
const int MAXN = 1100;

ifstream fin ("D.in");
ofstream fout ("D.out");

int N;
double a[MAXN], b[MAXN];

int main()
{
    int ntest; fin >> ntest;
    for (int test = 0; test < ntest; test++)
    {
    
    fin >> N;
    for (int i = 0; i < N; i++)
        fin >> a[i];
    for (int i = 0; i < N; i++)
        fin >> b[i];
    
    sort (a, a + N);
    sort (b, b + N);
    
    int blo = 0, bhi = N - 1;
    int res = 0;
    for (int i = 0; i < N; i++)
    {
        if (a[i] > b[blo])
        {
            res++;
            blo++;
        }
        else
            bhi--;
    }
    
    fout << "Case #" << test + 1 << ": " << res << " ";
    
    blo = 0, bhi = N - 1;
    res = 0;
    for (int i = N - 1; i >= 0; i--)
    {
        if (a[i] > b[bhi])
        {
            res++;
            blo++;
        }
        else
            bhi--;
    }
    
    fout << res << "\n";
    }
    
    //system ("Pause");
    return 0;
}
