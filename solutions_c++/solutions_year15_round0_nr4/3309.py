#include <iostream>
#include <fstream>

using namespace std;

#define RIC "RICHARD"
#define GAB "GABRIEL"

int main(){
    ifstream cin ("D-small-attempt7.in");
    ofstream cout("output.txt");

    int tc;
    cin >> tc;
    for (int c = 1; c <= tc; c++){
        int x, nr, nc;
        cin >> x >> nr >> nc;
        cout << "Case #" << c << ": ";

        if (nr % 2 == 1 && nc % 2 == 1 && x % 2 == 0){
            cout << RIC << endl;
        }
        else if (nr * nc > x && nr*nc < 2*x){
            cout << RIC << endl;
        }
        else if (nr < x && nc < x){
            cout << RIC << endl;
        }
        else if (nr*nc % x != 0){
            cout << RIC << endl;
        }
        else if (x == 3 && (nr == 1 || nc == 1)){
            cout << RIC << endl;
        }
        else if (x == 4 && (nr == 2 || nc == 2)){
            cout << RIC << endl;
        }
        else if (x == 4&& (nr == 1 || nc == 1)){
            cout << RIC << endl;
        }
        else cout << GAB << endl;
    }
    return 0;
}
