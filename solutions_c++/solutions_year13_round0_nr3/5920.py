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

unsigned long inverso(unsigned long int num){

    char invNum[30];
    unsigned long inv = 0;
    int len;
    int digito;

    sprintf(invNum,"%lu",num);

    len = strlen(invNum);

    while (num != 0) {
        digito = num % 10;
        inv = inv + digito * pow(10,len-1);
        len--;
        num = num / 10;
    }

    return inv;
}

int esPalindromo (unsigned long num) {

    unsigned long int inv;
    inv = inverso(num);

    if (num == inv)
        return 1;
    else
        return 0;

}


int main () {

    #ifndef ONLINE_JUDGE
		ifstream entrada("C-small-attempt0.in");
	#else
		#define entrada cin
	#endif

    #ifndef ONLINE_JUDGE
		ofstream salida("C-small-attempt0.out");
	#else
		#define salida cout
	#endif

    int casos, k = 0;

    entrada >> casos;

    while (k < casos) {

    int izq, der;
    int contador = 0;
    entrada >> izq >> der;

    for (int i = izq; i <= der; i++) {
        int raiz = sqrt(i);
        if (raiz * raiz == i) {
            if (esPalindromo(i)) {
                if (esPalindromo(raiz)) {
                    contador++;
                }
            }
        }
    }

    salida << "Case #" << k+1 <<": " << contador << endl;
    k++;
    }

return 0;
}
