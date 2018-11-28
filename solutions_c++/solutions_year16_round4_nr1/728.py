#include <iostream>
#include <fstream>

using namespace std;

int T[13][3][3];
string S[13][3];
const int F[3][2] = { {0, 2}, {1, 0}, {1, 2} };

void preproc()
{
    T[0][0][0] = 1;
    T[0][1][1] = 1;
    T[0][2][2] = 1;
    S[0][0] = 'R';
    S[0][1] = 'P';
    S[0][2] = 'S';
    for (int N = 1; N <= 12; N++)
    {
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                T[N][i][j] = T[N-1][F[i][0]][j] + T[N-1][F[i][1]][j];
            }
            if (S[N-1][F[i][0]] < S[N-1][F[i][1]])
                S[N][i] = S[N-1][F[i][0]] + S[N-1][F[i][1]];
            else
                S[N][i] = S[N-1][F[i][1]] + S[N-1][F[i][0]];
        }
    }
}

int main()
{
    preproc();
    //istream& in = cin;
    //tostream& out = cout;
    ifstream in("in.txt");
    ofstream out("out.txt");
    int X;
    in >> X;
    for (int t = 1; t <= X; t++)
    {
        int N, R, P, SS;
        in >> N >> R >> P >> SS;
        bool solved = false;
        for (int i = 0; i < 3; i++)
        {
            if ((T[N][i][0] == R) && (T[N][i][1] == P) && (T[N][i][2] == SS))
            {
                out << "Case #" << t << ": " << S[N][i] << endl;
                solved = true;
                break;
            }
        }
        if (!solved)
        {
            out << "Case #" << t << ": IMPOSSIBLE" << endl;
        }
    }
}
