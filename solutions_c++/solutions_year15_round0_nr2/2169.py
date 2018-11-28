#include <iostream>
#include <fstream>

using namespace std;

ifstream fin ("B.in");
ofstream fout ("B.out");

int N;
int arr[1100];

int main()
{
    int T; fin >> T;
    for (int test = 1; test <= T; test++)
    {
        fin >> N;
        for (int i = 0; i < N; i++)
            fin >> arr[i];
        
        int ans = 1e6;
        for (int i = 1; i <= 1000; i++)
        {
            int x = 0;
            for (int j = 0; j < N; j++)
                x += (arr[j] - 1) / i;
            ans = min (ans, x + i);
        }
        
        fout << "Case #" << test << ": " << ans << "\n";
    }
    return 0;
}
