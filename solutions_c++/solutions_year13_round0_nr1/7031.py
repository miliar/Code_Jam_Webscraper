#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
using namespace std;
const char JOKER='T';


bool Won(string tabla[], char c)
{
    bool jo;
    //sor
    for (int k=0;k<4; k++)
    {
        jo=true;
        for (int i=0; i<4; i++)
        {
            jo=jo && ((tabla[k][i]==c)|| (tabla[k][i]==JOKER) );

        }
        if (jo){return true;}
    }

    //oszlop
     for (int k=0;k<4; k++)
    {
       jo=true;
        for (int i=0; i<4; i++)
        {
            jo=jo && ((tabla[i][k]==c)|| (tabla[i][k]==JOKER) );
           // cout<< i <<k<< "  "<<jo<< tabla[i][k] <<" "<<c<< "\n";
        }
        if (jo){return true;}
    }

    //atlo1
        jo=true;
        for (int i=0; i<4; i++)
        {
            jo=jo && ((tabla[i][i]==c)|| (tabla[i][i]==JOKER) );
        }
        if (jo){return true;}

    //atlo2
    jo=true;
    for (int i=0; i<4; i++)
        {
            jo=jo && ((tabla[i][3-i]==c)|| (tabla[i][3-i]==JOKER) );
        }
        if (jo){return true;}
}


bool NoPoints(string tabla[])
{
    bool jo=true;
    for (int k=0; k<4; k++){
        for (int i=0; i<4; i++)
    {
        jo=jo &&(tabla[k][i]!='.');
    }}
    return jo;
}

int main()
{
    ifstream f( "A-large.in");
    ofstream fki;
    fki.open("Tic.out");
    string line;
    getline(f,line);
    int n=atoi(line.c_str());
    string tabla[4];
    for (int k=0; k<n; k++)
    {
        for (int i=0; i<4; i++)
        {
          getline(f,line);
          tabla[i]=line;
        }
        if (Won(tabla,'X')){ fki << "Case #" << k+1<<": X won\n";}
        else
        {
            if (Won(tabla,'O')){ fki << "Case #" << k+1<<": O won\n";}
            else
            {
                if (NoPoints(tabla)){fki << "Case #" << k+1<<": Draw\n";}
                else{fki << "Case #" << k+1<<": Game has not completed\n";}
            }
        }
        getline(f,line);
    }
    f.close();
    fki.close();
   /* for (int k=0; k<4; k++){
    for (int i=0; i<4; i++){cout << tabla[k][i];}}*/
    return 0;
}
