#include<fstream>

using namespace std;
static int _case = 1;
ifstream fin("input.txt");
ofstream fout("output.txt");
void result(int _r) {
    fout << "Case #" << _case << ": ";
    switch(_r) {
    case 1:
        fout << "X won" << endl;
        return;
    case 2:
        fout << "O won" << endl;
        return;
    case 3:
        fout << "Draw" << endl;
        return;
    case 4:
        fout << "Game has not completed" << endl;
        return;
    }
}
int legit(char a, char b, char c, char d)
{
    // XXXX
    if((a == b && a == c && a == d) && (a == 'X' || a == 'O')) return (a == 'X' ? 1 : 2);
    // XXXT
    if((a == b && a == c && 'T' == d) && (a == 'X' || a == 'O')) return (a == 'X' ? 1 : 2);
    // XXTX
    if((a == b && 'T' == c && a == d) && (a == 'X' || a == 'O')) return (a == 'X' ? 1 : 2);
    // XTXX
    if(('T' == b && a == c && a == d) && (a == 'X' || a == 'O')) return (a == 'X' ? 1 : 2);
    // TXXX
    if(('T' == a && b == c && b == d) && (b == 'X' || b == 'O')) return (a == 'X' ? 1 : 2);
    return 0;
}
void solve() {
    int totalX = 0, totalO = 0, totalT = 0;
    char in[4][4];
    int _p;
    for(int i = 0; i < 4; i++) {
        char a, b, c, d;
        fin >> a >> b >> c >> d;

        if(a == 'X') totalX++; if(b == 'X') totalX++; if(c == 'X') totalX++; if(d == 'X') totalX++;
        if(a == 'O') totalO++; if(b == 'O') totalO++; if(c == 'O') totalO++; if(d == 'O') totalO++;
        if(a == 'T') totalT++; if(b == 'T') totalT++; if(c == 'T') totalT++; if(d == 'T') totalT++;

        in[i][0] = a;
        in[i][1] = b;
        in[i][2] = c;
        in[i][3] = d;
    }

    if(_p = legit(in[0][0], in[0][1], in[0][2], in[0][3])) return result(_p);
    if(_p = legit(in[1][0], in[1][1], in[1][2], in[1][3])) return result(_p);
    if(_p = legit(in[2][0], in[2][1], in[2][2], in[2][3])) return result(_p);
    if(_p = legit(in[3][0], in[3][1], in[3][2], in[3][3])) return result(_p);


    if(_p = legit(in[0][0], in[1][0], in[2][0], in[3][0])) return result(_p);
    if(_p = legit(in[0][1], in[1][1], in[2][1], in[3][1])) return result(_p);
    if(_p = legit(in[0][2], in[1][2], in[2][2], in[3][2])) return result(_p);
    if(_p = legit(in[0][3], in[1][3], in[2][3], in[3][3])) return result(_p);

    if(_p = legit(in[0][0], in[1][1], in[2][2], in[3][3])) return result(_p);
    if(_p = legit(in[0][3], in[1][2], in[2][1], in[3][0])) return result(_p);
    if(totalX + totalO + totalT == 16) return result(3);
    else return result(4);
}

int main() {
    int total;
    fin >> total;
    while(total --) {
        solve();
        _case++;
    }
    return 0;
}
