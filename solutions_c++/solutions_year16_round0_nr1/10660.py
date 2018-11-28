#include <iostream>
#include <sstream>
using namespace std;
int main() {
    bool cifre[10];

    int c;
    cin >> c;

    int n[c];

    for (int i=0;i<c;i++) {
        cin >> n[i];
    }

    for (int i=0;i<c;i++) {
        for (int i=0;i<10;i++) {
            cifre[i] = false;
        }
        if (n[i] == 0) {
            cout << "Case #" << i+1 << ": INSOMNIA" << endl;
        } else {
            int cont = 1;
            while (true) {
                int numero = cont*n[i];

                stringstream ss;
                ss << numero;
                string str = ss.str();
                for (int i3=0;i3<str.length();i3++) {
                    string s(1, str[i3]);
                    stringstream ss2(s);
                    int cifra;
                    ss2 >> cifra;
                    cifre[cifra] = true;
                }
                bool fine = true;
                for (int i2=0;i2<10;i2++) {
                    if (!cifre[i2]) {
                        fine = false;
                        break;
                    }
                }
                if (fine) {
                    cout << "Case #" << (i+1) << ": " << numero << endl;
                    break;
                }
                cont++;
            }
        }
    }



}
