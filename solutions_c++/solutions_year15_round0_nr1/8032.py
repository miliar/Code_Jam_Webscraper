#include <fstream>

using namespace std;

ifstream fin("codejam.in");
ofstream fout("codejam.out");

int t, n, i, j;
int nr, pers;
string s;

int main()
{
    fin >> t;
    for (i=1; i<=t; i++)
    {
        fin >> n;
        fin >> s;
        nr=pers=0;
        for (j=0; j<=n; j++)
        {
            if (pers<j && s[j]!='0')
            {
                nr+=j-pers;
                pers+=j-pers;
            }
            pers+=s[j]-'0';
        }
        fout << "Case #" << i << ": " << nr << '\n';
    }
    fin.close();
    fout.close();
    return 0;
}
