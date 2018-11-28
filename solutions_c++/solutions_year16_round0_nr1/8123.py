#include<iostream>
using namespace std;

int main()
{
    int i;
    cin >> i;
    for(int n=0;n<i;++n) {
        int liczba;
        cin >> liczba;
        cout << "Case #" << n+1 << ": ";
        if(liczba ==0) {
            cout << "INSOMNIA" << endl;
        } else {
            int bylo = 0;
            bool tab[10]; 
            for(int n=0;n<10;n++) {
                tab[n] = false;
            }
            int tmp = liczba;
            int licznik = 1;
            while(bylo<10) {
                while(tmp > 0) {
                    int a = tmp%10;
                    tmp/=10;
                    if(tab[a] == false) {
                        ++bylo;
                        tab[a] = true;
                    }
                }
                ++licznik;
                tmp = liczba* licznik;
            }
            cout << (licznik-1)*liczba << endl;
        }
    }
}