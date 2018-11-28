#include <iostream>

using namespace std;

int testy;
double farma;
double zysk;
double cel;
double obecna;
double wynik;

int main()
{
    ios_base::sync_with_stdio(0);

    cin >> testy;

    cout.precision(15);

    for(int i=1;i<=testy;i++)
    {
        cin >> farma >> zysk >> cel;

        obecna=2;
        wynik=0;

        while(true)
        {

        if((cel-farma)/obecna<=cel/(obecna+zysk))
        {
            wynik=wynik+cel/obecna;
            cout << "Case #" << i << ": " << wynik << endl;
            break;
        }
        else
        {
            wynik=wynik+farma/obecna;
            obecna=obecna+zysk;
        }

        }
    }

    return 0;
}
