#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>

#define INF ~(1 << 31)

using namespace std;

int main(int argc, char *argv[]) {
    
    ifstream fin("repeat.in");
    ofstream fout("repeat.out");
    
    int T; fin >> T;
    int N = 0;
    for (int t = 1; t <= T; t++)
    {
        fin >> N;
        
        string s1, s2; fin >> s1 >> s2;
        int moves = 0;
        bool good = true;
        int i = 0, j = 0;
        while (true)
        {
            if (i == s1.size() && j == s2.size())
                break;
            
            if (i == s1.size() ^ j == s2.size())
            {
                good = false;
                break;
            }
            
            
            
            if (s1[i] == s2[j])
            {
                int k = i+1;
                while (k < s1.size() && s1[i] == s1[k]) k++;
                
                int h = j+1;
                while (h < s2.size() && s2[j] == s2[h]) h++;
                
                moves += abs((k-i)-(h-j));
                
                i = k;
                j = h;
                
            }
            else
            {
                good = false;
                break;
            }
        }
        if (good)
            fout << "Case #" << t << ": " << moves << "\n";
        else fout << "Case #" << t << ": Fegla Won\n";
    }
    
    fin.close();
    fout.close();
    return 0;
}