

#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <cstring>

using namespace std;
ofstream out("panka.out");
ifstream in("panka.in");

#define dim 109

int T;
int n;
int v[dim];

bool isCorect()
{
    if(n == 0)
        return true;

    for(int i = 1 ; i<=n; ++i)
        if(v[i] == -1)
            return false;
    return true;
}

void stergePlus()
{
    while(v[n] == 1)
    {
        --n;
    }
}

void faMinus()
{
    int i = 1;
    while(v[i] == 1)
    {
        v[i] = -1;
        ++i;
    }
}

int main()
{
    in >> T;
    for(int test = 1;  test<=T; ++test)
    {
        out << "Case " << "#" << test << ":" << " ";
        int sol = 0;
        string s;
        in >> s;
        n = 0;

        for(int i = 0 ; i < s.length(); ++i)
        {
            if(s[i] == '-')
            {
                v[++n] = -1;
            }
            else
            {
                v[++n] = 1;
            }
        }
        if(isCorect())
        {
            out << 0 << '\n';
        }
        else
        {
            while(!isCorect())
            {
                stergePlus(); // sterg secventa de 1 din partea dreapta
                //luam primul caz
                //daca avem minus la ambele capete facem interschimbare in tot sirul
                if(v[1] == v[n] && v[n] == -1)
                {
                    ++sol;
                    vector < int > copie;
                    for(int k = 1 ; k<=n; ++k)
                        copie.push_back(v[k]);
                    for(int k = copie.size() - 1; k >=0; --k)
                    {
                        if(copie[k] == -1)
                        {
                            v[k+1] = 1;
                        }
                        else
                        {
                            v[k+1] = -1;
                        }
                    }
                }
                else
                if(v[1] != v[n] && v[n] == -1 && v[1] == 1)
                {
                    ++sol;
                    faMinus();
                }
            }

            out << sol << '\n';
        }
    }
}
