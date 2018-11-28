#include <set>
#include <map>
#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
using namespace std;

string path = "/home/nicolai/work/CLionProjects/untitled/";

char mat[8][8] = { {0, 1, 2, 3, 4, 5, 6, 7 },
                   {1, 4, 3, 6, 5, 0, 7, 2 },
                   {2, 7, 4, 1, 6, 3, 0, 5 },
                   {3, 2, 5, 4, 7, 6, 1, 0 },
                   {4, 5, 6, 7, 0, 1, 2, 3 },
                   {5, 0, 7, 2, 1, 4, 3 ,6 },
                   {6, 3 ,0, 5, 2, 7, 4, 1 },
                   {7, 6, 1, 0, 3, 2, 5, 4 } };


int main() {
    int N;
    ifstream in(path + "input.txt");
    ofstream out(path + "output.txt");
    in >> N;
    for (int t = 0; t < N; t++) {
        long long l, x;
        in >> l >> x;
        if (x > 11)
            x = ((x - 11) % 4) + 11;
        while (x > 11)
            x -= 4;
        string str;
        in >> str;
        for (int i = 0; i < l; i++)
            str[i] = (str[i] == 'i' ? 1 : (str[i] == 'j' ? 2 : 3));
        vector<vector<char> > v(l + 1, vector<char>(l + 1, 0));
        for (int i = 0; i <= l; i++) {
            char c = 0;
            for (int j = i; j <= l; j++) {
                v[i][j] = c;
                c = mat[c][str[j]];
            }
        }
        char st[12];
        char c = v[0][l];
        for (char i = 0, j = 0; j <= x; j++, i = mat[i][c])
            st[j] = i;
        bool fl = false;
        for (int p1 = 0; p1 <= l && !fl; p1++) {
            for (int p2 = 0; p2 <= l && !fl; p2++) {
                // diff parts
                for (int i = 0; i <= x - 2; i++)
                    for (int j = 0; i + j <= x - 2; j++)
                        if (mat[st[i]][v[0][p1]] == 1 && mat[mat[v[p1][l]][st[j]]][v[0][p2]] == 2
                            && mat[v[p2][l]][st[x - i - j - 2]] == 3)
                            fl = true;
                // one part
                if (p1 < p2)
                    for (int i = 0; i <= x - 1; i++)
                        if (mat[st[i]][v[0][p1]] == 1 && v[p1][p2] == 2 && mat[v[p2][l]][st[x - 1 - i]] == 3)
                            fl = true;
            }
        }
        out << "Case #" << t + 1 << ": " << (fl ? "YES" : "NO") << endl;
    }
    return 0;
}

