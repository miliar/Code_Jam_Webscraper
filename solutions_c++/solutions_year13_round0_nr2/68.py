#include <string>
#include <iostream>
#include <vector>
#include <utility>
#include <cstdio>
using namespace std;

int a[200][200];
int N, M;
void init()
{
    cin >> N >> M;
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < M; ++j)
            cin >> a[i][j];
}

string deal()
{
    while (true)
    {
        int zeroCnt = 0;
        for (int i = 0; i < N; ++i)
            for (int j = 0; j < M; ++j)
                if (a[i][j] == 0) zeroCnt++;
        if (zeroCnt == N * M) return "YES";
        
        int minValue = 999;
        int ti, tj;
        for (int i = 0; i < N; ++i)
            for (int j = 0; j < M; ++j)
                if (a[i][j] > 0 && a[i][j] < minValue)
                {
                    minValue = a[i][j];
                    ti = i;
                    tj = j;
                }
        
        bool isRowOK = true;
        for (int j = 0; j < M; ++j)
        {
            if (a[ti][j] == minValue || a[ti][j] == 0) continue;
            isRowOK = false;
        }
        
        if (isRowOK)
        {
            for (int j = 0; j < M; ++j) a[ti][j] = 0;
            continue;
        }
        
        bool isColOK = true;
        for (int i = 0; i < N; ++i)
        {
            if (a[i][tj] == minValue || a[i][tj] == 0) continue;
            isColOK = false;
        }
        
        if (isColOK)
        {
            for (int i = 0; i < N; ++i) a[i][tj] = 0;
            continue;
        }
        return "NO";
    }
}

int main()
{
    freopen("/Users/pigoneand/windoflife/CONTEST/CODEJAM/QUAL/b.in", "r", stdin);
    freopen("/Users/pigoneand/windoflife/CONTEST/CODEJAM/QUAL/b.out", "w", stdout);
    
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test)
    {
        init();
        cout << "Case #" << test << ": " << deal() << endl;
    }
    return 0;
}