#include <iostream>
#include <fstream>
#include <stdlib.h>
using namespace std;


bool checkWinner(char tab[4][4], char sign);
bool checkIfOver(char tab[4][4]);

int main()
{
    fstream fp, fpOut; /* u¿ywamy metody wysokopoziomowej - musimy mieæ zatem identyfikator pliku, uwaga na gwiazdkê! */
    fp.open("A-large.in");
    fpOut.open("output.in");
    if (!fp.is_open()) {
     exit(1);
     }

	if (!fpOut.is_open()) {
     exit(1);
     };
	int T;
	string line, pom;
	getline(fp, line);
	T = atoi(line.c_str());
	char tab[4][4];

	for (int i = 0; i<T; i++)
	{
	    for (int j=0; j<4; j++)
	    {
	        getline(fp, pom);
	        for (int k=0; k<4; k++) tab[j][k]=pom[k];
	    }

    fpOut<<"Case #";
    if (checkWinner(tab, 'O'))
    {
          fpOut<<i+1<<": O won"<<endl;
    }
    else if (checkWinner(tab, 'X'))
    {
        fpOut<<i+1<<": X won"<<endl;
    }
    else if (!checkIfOver(tab))
    {
        fpOut<<i+1<<": Game has not completed"<<endl;
    }
    else fpOut<<i+1<<": Draw"<<endl;
	getline(fp, pom);

	}


    fp.close(); /* zamknij plik */
    return 0;
}

bool checkWinner(char tab[4][4], char sign)
{
    //---rank
    for(int i = 0; i<4; i++)
    {
        for (int j=0; j<4; j++)
        {
            if (tab[i][j] != sign && tab[i][j] != 'T') break;
            else if(j==3) return true;
        }
    }

    //---column
    for(int i = 0; i<4; i++)
    {
        for (int j=0; j<4; j++)
        {
            if (tab[j][i] != sign && tab[j][i] != 'T') break;
            else if(j==3) return true;
        }
    }

    //---diagonal
    for(int i = 0; i<4; i++)
    {
            if (tab[i][i] != sign && tab[i][i] != 'T') break;
            else if(i==3) return true;
    }
    for(int i = 0; i<4; i++)
    {
            if (tab[i][3-i] != sign && tab[i][3-i] != 'T') break;
            else if(i==3) return true;
    }

    return false;
}

bool checkIfOver(char tab[4][4])
{
    for(int i = 0; i<4; i++)
    {
        for (int j=0; j<4; j++)
        {
            if (tab[j][i] == '.') return false;
        }
    }
    return true;
}

