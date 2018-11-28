#include <iostream>
#include <cstdlib>
#include <vector>
#include <fstream>
#include <cmath>

#define ll long long

#define int long long

using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");

bool f(int x) {
    //cerr << "x = " << x;
    string s = "";
    while (x) {
        char c = '0' + (x % 10);
        s += c;
        x /= 10;
    }

    //cerr << "s = " << s << endl;

    int i = 0;
    int j = s.size() - 1;
    while (i < j) {
        if (s[i] != s[j]) return false;
        i++;
        j--;
    }
    return true;
}

#undef int

int main () {
    #define int long long
    int Tc;
    in >> Tc;
    for (int t=0; t < Tc; t++) {
        int a, b;
        in >> a >> b;
        double xx = sqrt(a);
        int x = (int) xx - 1;

        int result = 0;

        for (int i=x; i*i <= b; i++) {
            int y = i*i;
            if (y < a) continue;
            //cerr << y << " ";
            if (f(y) && f(i)) {
                //cerr << "yes";
                result ++;
            }

            //cerr << endl;
        }
        //cerr << endl;

        out << "Case #" << t+1 << ": " << result << endl;
        //cerr << endl;
    }

    /*for (int i=1; i <= 1000; i++) {
        f(i);
    }*/
}
