#include <map>
#include <cmath>
#include <cstring>
#include <string>

#include <vector>
#include <fstream>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <cctype>

using namespace std;

//#define ONLINE_JUDGE 1

unsigned long long calcular_area_inicial (unsigned long long r) {

    return r * r;

}

unsigned long long calcular_area_trazo (unsigned long long a1, unsigned long long a2) {

    return a2 - a1;

}

int main () {

    #ifndef ONLINE_JUDGE
		ifstream entrada("A-small-attempt0.in");
	#else
		#define entrada cin
	#endif

    #ifndef ONLINE_JUDGE
		ofstream salida("A-small-attempt0.out");
	#else
		#define salida cout
	#endif

    int casos, k = 0;

    entrada  >> casos;
    while (k < casos) {
        unsigned long long radio, pintura;
        entrada >> radio;
        entrada >> pintura;
        int flag  = 1;
        unsigned long long total = 0;
        unsigned long long acum = 0;
        while (flag) {
            unsigned long long area1 = calcular_area_inicial(radio);
            unsigned long long area2 = calcular_area_inicial(radio+1);
            unsigned long long area = calcular_area_trazo(area1,area2);
            acum+=area;
            if (acum <= pintura) {
                total+=1;
            }else {
                flag = 0;
            }
            radio +=2;
        }
        salida << "Case #" << ++k << ": " << total << endl;
    }

return 0;
}
