#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ifstream in;
    ofstream out;
    in.open("A-small-attempt0.in");
    out.open("A-small-attempt0.out");
    int r, t, N, br, a, count = 0;
    in >> N;
    for(int i = 0; i < N; i++) {
    count = 0;
    in >> r >> t;
        do {
            cout << "Trying circle radius " << r << ", I have " << t << "ml paint" << endl;
            br = r + 1;
            a = (br * br) - (r * r);
            cout << "Area: " << a << endl;
            if(a <= t) {
                 cout << "Enough paint!" << endl;
                 t -= a;
                 count++;
            }
            else
            {break;}
            r+=2;
            } while(t >= a);
        out << "Case #" << i + 1 << ": " << count << endl;
    }
}
