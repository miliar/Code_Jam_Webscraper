
#include <fstream>
#include <deque>
#include <vector>
#include <cstring>

using namespace std;

ifstream fin("googleB.in");
ofstream fout("googleB.out");
#define dim 20

int val[dim];
void detSol(string s)
{
    string copie = string(s);

    for (int i = 0; i < copie.length() && s.length() > 0; ++i)
    {
        if (copie[i] == 'Z')
        {
            s.erase(s.begin() + s.find('Z'));
            s.erase(s.begin() + s.find('E'));
            s.erase(s.begin() + s.find('R'));
            s.erase(s.begin() + s.find('O'));
            ++val[0];
        }
        else
        if (copie[i] == 'W')
        {
            s.erase(s.begin() + s.find('T'));
            s.erase(s.begin() + s.find('W'));
            s.erase(s.begin() + s.find('O'));
            ++val[2];
        }
        else
        if (copie[i] ==  'X')
        {
            s.erase(s.begin() + s.find('S'));
            s.erase(s.begin() + s.find('I'));
            s.erase(s.begin() + s.find('X'));
            ++val[6];
        }
        else
        if(copie[i] == 'G')
        {
            s.erase(s.begin() + s.find('E'));
            s.erase(s.begin() + s.find('I'));
            s.erase(s.begin() + s.find('G'));
            s.erase(s.begin() + s.find('H'));
            s.erase(s.begin() + s.find('T'));
            ++val[8];
        }
    }

    copie = string(s);
    for (int i = 0; i < copie.length() && s.length() > 0; ++i)
    {
        if (copie[i] == 'T')
        {
            s.erase(s.begin() + s.find('T'));
            s.erase(s.begin() + s.find('H'));
            s.erase(s.begin() + s.find('R'));
            s.erase(s.begin() + s.find('E'));
            s.erase(s.begin() + s.find('E'));
            ++val[3];
        }
        else
        if (copie[i] == 'S')
        {
            s.erase(s.begin() + s.find('S'));
            s.erase(s.begin() + s.find('E'));
            s.erase(s.begin() + s.find('V'));
            s.erase(s.begin() + s.find('E'));
            s.erase(s.begin() + s.find('N'));
            ++val[7];
        }
    }

    copie = string(s);
    for (int i = 0; i < copie.length() && s.length() > 0; ++i)
    {
        if (copie[i] == 'V')
        {
            s.erase(s.begin() + s.find('F'));
            s.erase(s.begin() + s.find('I'));
            s.erase(s.begin() + s.find('V'));
            s.erase(s.begin() + s.find('E'));
            ++val[5];
        }
    }

    copie = string(s);
    for (int i = 0; i < copie.length() && s.length() > 0; ++i)
    {
        if (copie[i] == 'F')
        {
            s.erase(s.begin() + s.find('F'));
            s.erase(s.begin() + s.find('O'));
            s.erase(s.begin() + s.find('U'));
            s.erase(s.begin() + s.find('R'));
            ++val[4];
        }
    }

    copie = string(s);
    for (int i = 0; i < copie.length() && s.length() > 0; ++i)
    {
        if (copie[i] == 'O')
        {
            s.erase(s.begin() + s.find('O'));
            s.erase(s.begin() + s.find('N'));
            s.erase(s.begin() + s.find('E'));
            ++val[1];
        }
    }

    copie = string(s);
    for (int i = 0; i < copie.length() && s.length() > 0; ++i)
    {
        if (copie[i] == 'N')
        {
            s.erase(s.begin() + s.find('N'));
            s.erase(s.begin() + s.find('I'));
            s.erase(s.begin() + s.find('N'));
            s.erase(s.begin() + s.find('E'));
            ++val[9];
        }
    }
}
void Solve(int test)
{

    string s;
    fin >> s;
    memset(val,0,sizeof(val));
    detSol(s);

    fout << "Case #" << test << ": ";
    for (int i = 0; i < 10; ++i) {
        for (int j = 1; j <= val[i]; ++j) {
            fout << i;
        }
    }
    fout << "\n";
}

int main()
{
    int T;
    fin >> T;
    for (int test = 1; test <= T; test++)
    {
        Solve(test);
    }
    return 0;
}
