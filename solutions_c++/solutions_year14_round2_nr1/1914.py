#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <cmath>
#define forn(i,n) for(int i = 0; i<(int) n; i++)

#define MAX 1048576
#define pb push_back
#define mp make_pair

using namespace std;
int _C,n;
string s[2];

ifstream fin("entrada.txt");
ofstream fout("salida.txt");

int cada [100][2];

int main()
{

    fin>>_C;
    forn(i,_C)
    {
        fout<<"Case #"<<i+1<<": ";
        forn(j,100) forn(k,2)
           cada[j][k]=0;
        int resp=0; fin>>n;
        forn(j,n)
            fin>>s[j];
        int cont = 0;
        string resp1[2];
        forn(a,2)
        {
            cont =0;
            resp1[a][0]=s[a][0];
            forn(j,s[a].size())
            if(s[a][j]==s[a][j+1])
                cada[cont][a]++;
            else
            {
                resp1[a]+=s[a][j];
                cont++;
            }
        }
        if(resp1[0]!=resp1[1]) fout<<"Fegla Won"<<endl;
        else
        {
            forn(i,cont)
                resp+=abs(cada[i][0]-cada[i][1]);

              fout<<resp<<endl;
        }
    }
    return 0;
}
