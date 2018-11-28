#include <iostream>

using namespace std;

int mapa[10];

int getNumbers(int m) {
    while(m > 0){
        int c = m % 10;
        //cout << n << endl;
        mapa[ c ] = 1;
        m/= 10;

    }
}

int main() {

    int n;
    cin>>n;

    int casos = 0;
    while(n--) {

        for(int i = 0; i < 10; i++) mapa[i] = 0;
        int m;
        cin>>m;
        if(m != 0) {
            bool bander = false;
            int cont = 0;
            int voy = 1;
            int ultimo;
            while(!bander){
               int y = m*voy;
               voy++;
               getNumbers(y);

               bander = true;
               //cout << "con " << y << " ya vi: ";
               for(int j = 0; j < 10; j++) {
                    if(mapa[j] == 0) {
                        bander = false;
                    } else {
                        //cout << j << " ";
                    }
               }
              // cout << endl;
                cont++;
                ultimo = y;
            }
            cout<<"Case #" << ++casos << ": " << ultimo << endl;

        }else {
            cout<<"Case #" << ++casos << ": INSOMNIA" <<endl;
        }
    }

    return 0;
}
