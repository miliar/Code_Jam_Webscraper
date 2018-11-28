#include <iostream>
#include <cmath>
#include <algorithm>
#include <fstream>
#include <string>
#include <vector>

#define getmax(a, b) ((a)>(b)) ? (a) : (b)
#define getmin(a, b) ((a)<(b)) ? (a) : (b)

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);

    ifstream in ("A-small-attempt0.in");
    ofstream out ("A-small-attempt0.out");
    int t;
    in >> t;
    for (int ti=1; ti<=t; ti++)
    {
        int f[4][4],s[4][4],fr,sr;
        in >> fr;
        fr--;
        for (int i=0; i<4; i++)
            for (int j=0; j<4; j++)
                in >> f[i][j];
        in >> sr;
        sr--;
        for (int i=0; i<4; i++)
            for (int j=0; j<4; j++)
                in >> s[i][j];
        int numCards=0,lastCardFound;
        for (int i=0; i<4; i++)
            for (int j=0; j<4; j++)
                if (f[fr][i]==s[sr][j])
                {
                    numCards++;
                    lastCardFound=f[fr][i];
                    break;
                }
        out << "Case #" << ti << ": ";
        if (numCards==0)
            out << "Volunteer cheated!\n";
        else if (numCards>1)
            out << "Bad magician!\n";
        else
            out << lastCardFound << '\n';
    }
    in.close();
    out.close();
}
