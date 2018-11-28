#include <iostream>
#include <fstream>
#include <unordered_map>
#include <cstring>
#include <queue>
#include <algorithm>
#include <vector>
#include <math.h>
#include <unordered_set>

using namespace std;

int T;

int main()
{
    ifstream fin("A-small.in");
    ofstream fout("A-small.out");
    fin >> T;
    for (int i = 0; i < T; ++ i)
    {
        char s[101];
        int x[26] = {};
        fin >> s;
        int ls = strlen(s);
        for (int j = 0; j < ls; ++ j)
        {
            x[s[j] - 'A'] ++;
        }
        int ans[10] = {};
        char a[10][10] = {"ZERO", "EIGHT", "SIX", "THREE", "SEVEN", "FIVE", "FOUR", "TWO", "NINE", "ONE"};
        int b[10] = {0, 8, 6, 3, 7, 5, 4, 2, 9, 1};
        for (int j = 0; j < 10; ++ j)
        {
            int num = 100;
            //cout <<b[j] << ' ' << strlen(a[j]) << endl;
            for (int k = 0; k < strlen(a[j]); ++ k)
            {
                if (num > x[a[j][k] - 'A'])
                {
                    num = x[a[j][k] - 'A'];
                }
            }
            //cout <<num << endl;
            ans[b[j]] = num;
            for (int k = 0; k < strlen(a[j]); ++ k)
            {
                x[a[j][k] - 'A'] -= num;
            }
        }
        fout << "Case #" << i + 1 << ": ";
        for (int j = 0; j < 10; ++ j)
        {
            for (int k = 0; k < ans[j]; ++ k)
            {
                fout << j;
            }
        }
        fout << endl;
    }
    return 0;
}



