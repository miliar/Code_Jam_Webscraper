#include <iostream>
#include <fstream>

using namespace std;

fstream in, out;

void solve()
{
    int f[4][4], s[4][4], fg, sg;

    in >> fg;
    for(int i = 0; i < 4; ++i)
        for(int j = 0; j < 4; ++j)
            in >> f[i][j];

    in >> sg;
    for(int i = 0; i < 4; ++i)
        for(int j = 0; j < 4; ++j)
            in >> s[i][j];

    int c = 0, e = 0;
    for(int j = 0; j < 4; ++j)
        for(int k = 0; k < 4; ++k)
            if (f[fg-1][j] == s[sg-1][k]) 
            {
                e = f[fg-1][j];
                ++c;
            }

    if (c == 0) out << "Volunteer cheated!";
    else if (c > 1) out << "Bad magician!";
    else out << e;

}


int main()
{
    in.open("a.txt"); out.open("out.txt"); 
    int T;
    in >> T;

    for(int i = 1; i <= T; ++i)
    {
        out << "Case #" << i << ": ";
        solve(); 
        out << endl;
    }

    return 0;
}
