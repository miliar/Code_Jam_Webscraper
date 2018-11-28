#include <iostream>
#include <fstream>
#include <cstring>
#include <algorithm>

using namespace std;

ifstream fin("in.txt");
ofstream fout("out.txt");
bool filledMap[25];

int dr[] = {-1, -1, -1, 0, 1, 1, 1, 0};
int dc[] = {-1, 0, 1, 1, 1, 0, -1, -1};

void printFullMap(int R, int C)
{
    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            fout << (r+1==R && c+1==C? 'C' : '*');
        }
        fout << "\n";
    }
}

void printMap(int R, int C, int cr, int cc, bool map[25])
{
    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            fout << (r==cr && c==cc? 'C' : (map[r*C+c] ? '*' : '.'));
        }
        fout << "\n";
    }
}

bool isValid(int R, int C, int r, int c)
{
    return r >= 0 && r < R && c >= 0 && c < C;
}

int ccount = 0;

void floodfill(int R, int C, int r, int c, bool zeroMap[25], bool map[25])
{
    map[r*C+c] = 1;
    for (int d = 0; d < 8; d++) {
        int nr = r+dr[d], nc = c+dc[d];
        if (isValid(R, C, nr, nc) && !map[nr*C+nc]) {
            if (zeroMap[nr*C+nc]) floodfill(R, C, nr, nc, zeroMap, map);
            map[nr*C+nc] = 1;
        }
    }
}

bool chain(int R, int C, int i, int m, bool map[25])
{
    if (i == R*C) {
        bool dmap[25];
        bool zeroMap[25] = {0};
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (map[r*C+c]) continue;
                int d;
                for (d = 0; d < 8; d++) {
                    if (isValid(R, C, r+dr[d], c+dc[d]) && map[(r+dr[d])*C+c+dc[d]]) break;
                }
                zeroMap[r*C+c] = d == 8;
            }
        }
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (zeroMap[r*C+c]) {
                    memcpy(dmap, map, R*C);
                    floodfill(R, C, r, c, zeroMap, dmap);
                    if (!memcmp(dmap, filledMap, R*C)) {
                        printMap(R, C, r, c, map);
                        return true;
                    }
                }
            }
        }
        return false;
    }
    if (m > 0) {
        map[i] = 1;
        if (chain(R, C, i+1, m-1, map)) return true;
    }
    if (R*C - i > m) {
        map[i] = 0;
        if (chain(R, C, i+1, m, map)) return true;
    }
    return false;
}

int main()
{
    memset(filledMap, 1, 25);
    int T;
    fin >> T;
    for (int t = 1; t <= T; t++) {
        fout << "Case #" << t << ":\n";
        int R, C, M;
        fin >> R >> C >> M;
        if (M+1 == R*C)
            printFullMap(R, C);
        else {
            bool map[25];
            if (!chain(R, C, 0, M, map))
                fout << "Impossible\n";
        }
    }
}