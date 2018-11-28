#include <cstdio>
#include <cstdlib>
#include <string>
#include <fstream>

using namespace std;

string inPath = "A-small-attempt0.in";
string outPath = "A-small-attempt0.out";

int main(int argc, char** argv) {
    ifstream fin(inPath.c_str(), ifstream::in);
    ofstream fout(outPath.c_str(), ofstream::out);
    
    int tcases;
    fin >> tcases;
    
    for(int tcase = 0; tcase < tcases; ++tcase) {        
        int a[4][4], b[4][4], r1, r2;
        
        fin >> r1;
        for(int i = 0; i < 4; ++i)
            for(int j = 0; j < 4; ++j)
                fin >> a[i][j];
        fin >> r2;
        for(int i = 0; i < 4; ++i)
            for(int j = 0; j < 4; ++j)
                fin >> b[i][j];
        
        int cnt = 0, ans = 0;
        r1--;
        r2--;
        
        for(int i = 0; i < 4; ++i)
            for(int j = 0; j < 4; ++j)
                if(a[r1][i] == b[r2][j])
                    cnt++, ans = a[r1][i];
          
        if(cnt == 1)
            fout << "Case #" << tcase+1 << ": " << ans << "\n";
        else if(cnt > 1)
            fout << "Case #" << tcase+1 << ": " << "Bad magician!" << "\n";
        else
            fout << "Case #" << tcase+1 << ": " << "Volunteer cheated!" << "\n";
    }
    
    return 0;
}

