#include <iostream>
#include <vector>
#include <string>
#include <fstream>
using namespace std;

int makeHappy(string s, int end, int moves) {

    //Base cases
    if(end == 0 && s[0] == '+') {
        return moves;
    }
    else if(end == 0 && s[0] == '-') {
        return moves + 1;
    }

    //Already happy
    if(s[end] == '+') {
        return makeHappy(s, end - 1, moves);
    }
    //Otherwise flip everything and call function
    else {
        for(int i = 0; i <= end; i++) {
            if(s[i] == '+')
                s[i] = '-';
            else
                s[i] = '+';
        }
        return makeHappy(s, end - 1, moves + 1);
    }
}

int main() {
    fstream in("B-large.in", ios::in);
    fstream out("pancake.out", ios::out);
    int t;
    in >> t;
    for(int cas = 1; cas <= t; cas++) {
        string s;
        in >> s;
        out << "Case #" << cas << ": " << makeHappy(s, s.length() - 1, 0) << endl;
    }
    in.close();
    out.close();
    return 0;
}
