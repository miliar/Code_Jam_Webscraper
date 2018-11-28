#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstring>

using namespace std;

int getInt(ifstream &instream)
{
    string s = "";
    instream >> s;
    return atoi(s.c_str());
}

bool rowHasLarger(int **pLawn, int i, int j, int m)
{
    for (int k = 0; k < m; ++k) {
        if (pLawn[i][k] > pLawn[i][j]) return true;
    }
    return false;
}

bool colHasLarger(int **pLawn, int i, int j, int n)
{
    for (int l = 0; l < n; ++l) {
        if (pLawn[l][j] > pLawn[i][j]) return true;
    }
    return false;
}

// n行 * m列
bool isPossiblePattern(int **pLawn, int n, int m)
{
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (rowHasLarger(pLawn, i, j, m) && colHasLarger(pLawn, i, j, n)) return false;
        }
    }
    return true;
}

int main()
{
    ifstream si;
    si.open("B-large.in", fstream::in);
    ofstream so;
    so.open("blo.txt", fstream::out);
    
    int t = getInt(si);
    cout << t << endl;

    for (int i = 0; i < t; ++i) {
        // n行 * m列
        int n = getInt(si);
        int m = getInt(si);
        cout << n << " " << m << endl;
        int **pLawn = new int *[n];
        for (int j = 0; j < n; ++j) {
            pLawn[j] = new int[m];
        }
        for (int j = 0; j < n; ++j) {
            for (int k = 0; k < m; ++k) {
                pLawn[j][k] = getInt(si);
                cout << pLawn[j][k] << " ";
            }
            cout << endl;
        }
        so << "Case #" << i+1 << ": ";
        if (isPossiblePattern(pLawn, n, m)) so << "YES" << endl;
        else so << "NO" << endl;
        for (int j = 0; j < n; ++j) {
            delete [] pLawn[j];
        }
        delete [] pLawn;
    }

    si.close();
    so.close();

    return 0;
}

