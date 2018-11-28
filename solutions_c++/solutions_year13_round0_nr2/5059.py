#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int judge(vector< vector<int> > g, int w, int h) {
    int colmax[w], rowmax[h];
    
    for (int y = 0; y < h; y++) {
        int max = 0;
        for (int x = 0; x < w; x++) {
            if ( g[y][x] > max )
                max = g[y][x];
        }
        rowmax[y] = max;
    }
    
    for (int x = 0; x < w; x++) {
        int max = 0;
        for (int y = 0; y < h; y++) {
            if ( g[y][x] > max )
                max = g[y][x];
        }
        colmax[x] = max;
    }
    for (int x = 0; x < w; x++) {
        for (int y = 0; y < h; y++) {
            if ( g[y][x] < colmax[x] &&  g[y][x] < rowmax[y] )
                return 0;
        }
    }
    return 1;
}

int main(int argc, char *argv[])
{
    int count;
    ifstream fin("B-large.in");
    ofstream fout("output");
    fin >> count;
    for (int c = 0; c < count; c++) {
        int h, w;
        fin >> h >> w;
        vector< vector<int> > g(h);
        
        for (int y = 0; y < h; y++) {
            g[y].resize(w);
            for (int x = 0; x < w; x++) {
                fin >> g[y][x];
            }
        }

        fout << "Case #" << c + 1 << ": ";
        if ( judge(g, w, h) ) {
            fout << "YES" << endl;
        } else {
            fout << "NO" << endl;
        }
    }
    
    system("PAUSE");
    return EXIT_SUCCESS;
}
