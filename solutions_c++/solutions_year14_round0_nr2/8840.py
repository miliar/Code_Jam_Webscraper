#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;

int main() {
    int ilt;
    cin >> ilt;
    for (int tn = 1; tn <= ilt; ++tn) {
        double koszt_f, daje_f, ile_need;
        cin >> koszt_f >> daje_f >> ile_need;

        double wynik = ile_need / 2.;
        double koszt_farm = 0.;
        for (int ile_farm = 1; koszt_farm < wynik; ++ile_farm) {
            koszt_farm += koszt_f / (2. + (ile_farm - 1) * daje_f);
            wynik = min(wynik, koszt_farm + ile_need / (2. + ile_farm * daje_f));
        }
        cout << "Case #" << tn << ": " << setprecision(12) << wynik << endl;
    }
}
