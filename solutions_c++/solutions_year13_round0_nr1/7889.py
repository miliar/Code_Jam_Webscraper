#include <queue>
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
#include <cstring>
#include <algorithm>
#include <utility>

using namespace std;


#define DIMENSIONE 4

char A[DIMENSIONE][DIMENSIONE];



bool completato()
{
    for(int i=0; i < DIMENSIONE; i++)
        for(int j=0; j < DIMENSIONE; j++)
            if(A[i][j]=='.')
                return false;
    return true;
}


char vincitore(int p){
	if(p==2*2*2*5 || p==2*2*2*2)
		return 'X';
	else if(p==3*3*3*5 || p==3*3*3*3)
		return 'O';
	else
		return 'N';
}


void chi_vince()
{

    int i, j;
	for(i=0; i < DIMENSIONE; i++){
        int prodotto_righe=1;
		for(j=0; j < DIMENSIONE; j++)
		{
			if(A[i][j]=='X')
				prodotto_righe*=2;
			else if(A[i][j]=='O')
				prodotto_righe*=3;
			else if(A[i][j]=='T')
				prodotto_righe*=5;
		}
		char w=vincitore(prodotto_righe);
		if(w!='N')
		{
			cout << w << " won" << endl;
			return;
		}
	}

	for(i=0; i < DIMENSIONE; i++)
	{
        int prodotto_colonne=1;
		for(j=0; j < DIMENSIONE; j++){
			if(A[j][i]=='X')
				prodotto_colonne*=2;
			else if(A[j][i]=='O')
				prodotto_colonne*=3;
			else if(A[j][i]=='T')
				prodotto_colonne*=5;
		}
		char w=vincitore(prodotto_colonne);
		if(w!='N'){
			cout << w << " won" << endl;
			return;
		}
	}

    int prodotto_diagonali=1;
	for(i=0; i < DIMENSIONE; i++)
	{
		if(A[i][i]=='X')
			prodotto_diagonali*=2;
		else if(A[i][i]=='O')
			prodotto_diagonali*=3;
		else if(A[i][i]=='T')
			prodotto_diagonali*=5;

		char w=vincitore(prodotto_diagonali);
		if(w!='N'){
			cout << w << " won" << endl;
			return;
		}
	}

    prodotto_diagonali=1;
	for(i=0; i < DIMENSIONE; i++){
		if(A[i][DIMENSIONE-1-i]=='X')
			prodotto_diagonali*=2;
		else if(A[i][DIMENSIONE-1-i]=='O')
			prodotto_diagonali*=3;
		else if(A[i][DIMENSIONE-1-i]=='T')
			prodotto_diagonali*=5;

		char w=vincitore(prodotto_diagonali);
		if(w!='N')
		{
			cout << w << " won" << endl;
			return;
		}
	}


	if(completato())
	{
		cout << "Draw" << endl;
	}
	else
		cout << "Game has not completed" << endl;


}

int main (int argc, char *argv[])
{

      freopen("input.in","r",stdin);
      freopen("output.out","w",stdout);


    int T;
    cin >> T;
    for(int i=0; i < T; i++){
        for(int j =0; j < DIMENSIONE; j++)
            for(int k = 0; k < DIMENSIONE; k++){

                cin >> A[j][k];
            }
        cout << "Case #" << i+1 << ": ";
        chi_vince();
    }



    return 0;
}
