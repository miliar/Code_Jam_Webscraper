#include <iostream>

using namespace std;

int main()
{
    int T, k, licznik = 0, ilosc_widzow = 0;
    string widownia;
    cin >> T;
    for(int i = 1; i <= T; i++)
    {
        cin >> k >> widownia;
        ilosc_widzow += widownia[0]-48;
        for(int j = 1; j <= k; j++)
        {
            if((j > ilosc_widzow) && (widownia[j] != 48))
            {
                licznik += j - ilosc_widzow;
                ilosc_widzow += j - ilosc_widzow;
            }
            ilosc_widzow += widownia[j]-48;
        }
        cout << "Case #" << i << ": " << licznik << endl;
        licznik = 0;
        ilosc_widzow = 0;
    }
    return 0;
}
