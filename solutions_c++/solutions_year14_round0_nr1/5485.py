#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>

#define INF ~(1 << 31)
#define LEN 4

using namespace std;
int main(int argc, char *argv[]) {
    
    ifstream fin("magic.in");
    ofstream fout("magic.out");
    
    int T; fin >> T;
    int R, v;
    for (int c = 1; c <= T; c++)
    {
        int cnt = 0;
        fin >> R;
        set<int> s;
        vector<int> matches;
        for (int r = 1; r <= LEN; r++)
        {
            for (int i = 0; i < LEN; i++)
            {
                fin >> v; 
                if (r == R)
                {
                    if (s.find(v) == s.end())
                        s.insert(v);
                    else
                        matches.push_back(v);
                }  
            }         
        }
        fin >> R;
        for (int r = 1; r <= LEN; r++)
        {
            for (int i = 0; i < LEN; i++)
            {
                fin >> v;
                if (r == R)
                {
                    if (s.find(v) == s.end()) s.insert(v);
                    else matches.push_back(v);
                }
            }
        }
        if (matches.size() > 1)
        {
            fout << "Case #" << c << ": Bad magician!\n";
        }
        else
        {
            if (matches.size() == 0)
            {
                fout << "Case #" << c << ": Volunteer cheated!\n";
            } else fout << "Case #" << c << ": " << matches[0] << "\n";
        }
    }
    
    fin.close();
    fout.close();
    return 0;
}