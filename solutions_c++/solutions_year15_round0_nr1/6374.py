/*
ID: 
PROG: 
LANG: C++
*/

#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>

#define INF ~(1 << 31)
#define MAXL 1001

using namespace std;

int aud[MAXL];

int main(int argc, char *argv[]) {
    ifstream fin("a.in");
    ofstream fout("a.out");
        
    int C; fin >> C;
    for (int c = 1; c <= C; c++)
    {
        int len; fin >> len;
        len++;
        
        char ch;
        for (int i = 0; i < len; i++)
        {
            fin >> ch;
            aud[i] = ch - '0';
        }
        
        int ans = 0;
        int standing = aud[0];
        for (int i = 1; i < len; i++)
        {
            if (standing < i)
            {
                ans += i - standing;
                standing = i;
            }
            standing += aud[i];
        }
        fout << "Case #" << c << ": " << ans << "\n";
    }
    
    return 0;
}