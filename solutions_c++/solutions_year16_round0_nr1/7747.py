#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {

    ifstream input("file.in");
    ofstream output("test.out");

    int n;
    input >> n;

    for(int i = 0; i < n; ++i) {
        int a;
        input >> a;

        vector<bool> nb(10, false);

        int b = 0;
        bool c = true;

        if(a == 0) {
            output << "Case #" << i + 1 << ": INSOMNIA" << endl;
            cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
        } else {
            while(c) {
                b += a;

                int d = b;
                while(d != 0) {
                    nb[d % 10] = true;
                    d /= 10;
                }

                c = false;
                for(int ii = 0; ii < 10; ++ii) {
                    if(!nb[ii]) {
                        c = true;
                        break;
                    }
                }

            }
            output << "Case #" << i + 1 << ": " << b << endl;
            cout << "Case #" << i + 1 << ": " << b << endl;
        }
    }

}
