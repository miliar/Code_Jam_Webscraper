#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct GCase
{
    int N, M;
    int** lawn;
    bool checkPattern()
    {
        int *xMax = new int[M];
        int *yMax = new int[N];
        for (int y = 0; y < N; ++y)
        {
            yMax[y] = 0;
            for (int x = 0; x < M; ++x)
            {
                if (lawn[y][x] > yMax[y])
                    yMax[y] = lawn[y][x];
            }
        }
        for (int x = 0; x < M; ++x)
        {
            xMax[x] = 0;
            for (int y = 0; y < N; ++y)
            {
                if (lawn[y][x] > xMax[x])
                    xMax[x] = lawn[y][x];
            }
        }
        //for (int i = 1; i < 100; ++i)
        {
            for (int y = 0; y < N; ++y)
            {
                for (int x = 0; x < M; ++x)
                {
                    if (lawn[y][x] < yMax[y] && lawn[y][x] < xMax[x])
                        return false;
                }
            }
        }
        return true;
    }
};

int g_nCases = 0;
vector<GCase*> g_cases;

void read_input()
{
    cin >> g_nCases;
    for (int i = 0; i < g_nCases; ++i)
    {
        GCase* gc = new GCase;
        // do sth
        cin >> gc->N >> gc->M;
        gc->lawn = new int*[gc->N];
        for (int y = 0; y < gc->N; ++y)
        {
            gc->lawn[y] = new int[gc->M];
            for (int x = 0; x < gc->M; ++x)
            {
                cin >> gc->lawn[y][x];
            }
        }
        g_cases.push_back(gc);
    }
}

int main(int argc, char**argv)
{
    read_input();

    for (int i = 0; i < g_nCases; ++i)
    {
        bool b = g_cases[i]->checkPattern();
        cout << "Case #" << i+1 << ": " ;
        if (b)
            cout << "YES";
        else
            cout << "NO";
        cout << endl;
    }
    return 0;
}
