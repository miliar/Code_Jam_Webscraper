#include <fstream>
#include <string>
using namespace std;

ifstream fin ("input");
ofstream fout ("output");

string mat[5];

inline int line (int line,char ch) {
    int cnt=0;

    for (int i=0; i<4; ++i)
        if (mat[line][i]==ch || mat[line][i]=='T')
            ++cnt;

    if (cnt==4)
        return 1;
    return 0;
}

inline int column (int column,char ch) {
    int cnt=0;

    for (int i=0; i<4; ++i)
        if (mat[i][column]==ch || mat[i][column]=='T')
            ++cnt;

    if (cnt==4)
        return 1;
    return 0;
}

inline int diag1 (char ch) {
    int cnt=0;

    for (int i=0; i<4; ++i)
        if (mat[i][i]==ch || mat[i][i]=='T')
            ++cnt;

    if (cnt==4)
        return 1;
    return 0;
}

inline int diag2 (char ch) {
    int cnt=0;

    for (int i=0; i<4; ++i)
        if (mat[i][3-i]==ch || mat[i][3-i]=='T')
            ++cnt;

    if (cnt==4)
        return 1;
    return 0;
}

inline int draw () {
    for (int i=0; i<4; ++i)
        for (int j=0; j<4; ++j)
            if (mat[i][j]!='X' && mat[i][j]!='O' && mat[i][j]!='T')
                return 0;
    return 1;
}

int main () {
    int T; fin>>T;
    for (int t=1; t<=T; ++t) {
        for (int i=0; i<4; ++i)
            fin>>mat[i];

        int winner=0;
        for (int i=0; i<4 && !winner; ++i) {
            if (line (i,'X') || column (i,'X'))
                winner='X';
            if (line (i,'O') || column (i,'O'))
                winner='O';
        }

        if (!winner && (diag1 ('X') || diag2 ('X')))
            winner='X';
        if (!winner && (diag1 ('O') || diag2 ('O')))
            winner='O';

        if (! winner && draw ())
            winner='N';

        if (winner=='X')
            fout<<"Case #"<<t<<": X won\n";
        else if (winner=='O')
            fout<<"Case #"<<t<<": O won\n";
        else if (winner=='N')
            fout<<"Case #"<<t<<": Draw\n";
        else
            fout<<"Case #"<<t<<": Game has not completed\n";
    }

    return 0;
}
