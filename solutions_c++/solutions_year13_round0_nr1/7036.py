#include <map>
#include <cmath>
#include <cstring>
#include <vector>
#include <fstream>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <cctype>

using namespace std;

//#define ONLINE_JUDGE 1
#define TAM 4

int main () {

    #ifndef ONLINE_JUDGE
		ifstream entrada("A-large.in");
	#else
		#define entrada cin
	#endif

    #ifndef ONLINE_JUDGE
		ofstream salida("A-large.out");
	#else
		#define salida cout
	#endif


	int k = 0, casos;
    entrada >> casos;

    while ( k < casos) {

        char caracter;

        int winner = 0;

        int columnaX[TAM];
        int columnaO[TAM];
        int diag1X = 0;
        int diag2X = 0;

        int diag1O = 0;
        int diag2O = 0;
        int it1 = 0;
        int it2 = 3;


        for (int i = 0; i < TAM; i++) {
            columnaO[i] = 0;
            columnaX[i] = 0;
        }

        int empate = 1;
        char cad;
        for (int i = 0; i < TAM; i++) {
            int filaX = 0;
            int filaO = 0;
            for (int j = 0; j < TAM; j++) {
                entrada >> caracter;

                if (caracter == 'X') {
                    columnaX[j]+=1;
                    filaX +=1;

                    if (i == j) {
                        diag1X +=1;
                    }
                    if (i == it1 && j == it2) {
                         diag2X +=1;
                    }

                }else if (caracter == 'O') {
                    columnaO[j]+=1;
                    filaO+=1;

                    if (i == j) {
                        diag1O += 1;
                    }

                    if (i == it1 && j == it2) {
                         diag2O +=1;
                    }

                }else if (caracter == 'T') {
                    columnaX[j]+=1;
                    columnaO[j]+=1;
                    filaO+=1;
                    filaX+=1;

                    if (i == j) {
                        diag1O+=1;
                        diag1X+=1;
                    }

                     if (i == it1 && j == it2) {
                         diag2O +=1;
                         diag2X +=1;
                    }

                }else {
                    empate = 0;
                }
            }

             if (filaX == 4) {
                cad = 'X';
                winner = 1;
            }

            if (filaO == 4) {
                cad = 'O';
                winner = 1;
            }
            it1++;
            it2--;
        }

        for (int i = 0; i < 4; i++) {
            if (columnaO[i] == 4) {
                cad = 'O';
                winner = 1;
            }

            if (columnaX[i] == 4) {
                cad = 'X';
                winner = 1;
            }
        }

        if ((diag1O) == 4) {
            cad = 'O';
            winner = 1;
        }

        if ((diag1X) == 4) {
            cad = 'X';
            winner = 1;
        }

        if ((diag2X) == 4) {
            cad = 'X';
            winner = 1;
        }

        if ((diag2O) == 4) {
            cad = 'O';
            winner = 1;
        }


        k++;

        if (winner == 1) {
            salida << "Case #" << k << ": " << cad << " won" << endl;
        }else {
            if (empate == 0) {
                salida << "Case #" << k <<": Game has not completed"<< endl;
            }else {
                salida << "Case #" << k << ": Draw" << endl;
            }
        }

    }

return 0;

}
