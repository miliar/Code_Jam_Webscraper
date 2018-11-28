#include <iostream>
#include <cstring>
#include <cmath>
#include <sstream>
#include <fstream>

using namespace std;

long long MAX = 100000000000000;
long long MAX_PAL = 9420645460249;

bool isPal(long long number){
    string s;
    stringstream out;
    out << number;
    s = out.str();
    int len = s.length();

    for (int i = 0; i < len/2; i++){
        if (s[i] != s[len-1-i]){
            return false;
        }
    }
    return true;
}

int main(){
    int perfectSqCount = 0;

    long long *perfect_squares = new long long[60];
    long long *perfect_squares_root = new long long[60];
    int k = 0;

    long long i = 1;
    long long max_i = sqrt(MAX_PAL);
    while (i <= max_i){
        long long perfectSq = i*i;
        if (perfectSq <= MAX){
            if (isPal(i) && isPal(perfectSq)){
                perfect_squares_root[k] = i;
                perfect_squares[k++] = perfectSq;
                perfectSqCount++;
            }
        }

        i++;
    }

    ifstream cin ("input.txt");
    ofstream cout("output.txt");

    int nC;
    cin >> nC;
    for (int c = 1; c <= nC; c++){
        long long nA, nB;
        cin >> nA >> nB;

        int a, b;
        a = 0;
        b = k;
        while (a < k){
            if (perfect_squares[a] >= nA)
                break;
            a++;
        }

        while (b >= a){
            if (perfect_squares[b] <= nB)
                break;
            b--;
        }

        cout << "Case #" << c << ": " << b-a+1 << endl;
    }

    return 0;
}
