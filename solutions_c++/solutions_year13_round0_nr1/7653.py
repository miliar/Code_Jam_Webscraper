#include <fstream>
#include <iostream>
#include <vector>
#include <string>

class ProblemA
{
    public:
        void solve();

    private:

};

void ProblemA::solve()
{
    std::ifstream fin("A-large.in");
    std::ofstream fout("a.out");

    int t;
    fin >> t;
    for ( int test = 1; test <= t; ++test )
    {
        fout << "Case #" << test << ": ";
        std::vector < std::string > area( 4, "" );
        for ( int i = 0; i < 4; fin >> area[i++] );
        std::string res = "Draw";
        for ( int i = 0; i < 4; ++i )
        {
            for ( int j = 0; j < 4; ++j )
            {
                if ( area[i][j] == '.' )
                {
                    res = "Game has not completed";
                }
            }
        }
        for ( int i = 0; i < 4; ++i )
        {
            int x = 0, o = 0, t = 0;
            for ( int j = 0; j < 4; ++j )
            {
                x += area[i][j] == 'X';
                o += area[i][j] == 'O';
                t += area[i][j] == 'T';
            }
            if ( o + t == 4 ) res = "O won";
            if ( x + t == 4 ) res = "X won";
        }
        for ( int j = 0; j < 4; ++j )
        {
            int x = 0, o = 0, t = 0;
            for ( int i = 0; i < 4; ++i )
            {
                x += area[i][j] == 'X';
                o += area[i][j] == 'O';
                t += area[i][j] == 'T';
            }
            if ( o + t == 4 ) res = "O won";
            if ( x + t == 4 ) res = "X won";
        }
        {
            int x = 0, o = 0, t = 0;
            for ( int i = 0; i < 4; ++i )
            {
                x += area[i][i] == 'X';
                o += area[i][i] == 'O';
                t += area[i][i] == 'T';
            }
            if ( o + t == 4 ) res = "O won";
            if ( x + t == 4 ) res = "X won";
        }
        {
            int x = 0, o = 0, t = 0;
            for ( int i = 0; i < 4; ++i )
            {
                x += area[3-i][i] == 'X';
                o += area[3-i][i] == 'O';
                t += area[3-i][i] == 'T';
            }
            if ( o + t == 4 ) res = "O won";
            if ( x + t == 4 ) res = "X won";
        }
        fout << res << std::endl;
    }

    fin.close();
    fout.close();
}


int main()
{
    ProblemA O;
    O.solve();
    return 0;
}
