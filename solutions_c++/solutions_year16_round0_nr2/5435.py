#include <iostream>
#include <string>
using namespace std;

int main() {
    int T, TT=1;
    string S;
    cin >> T;
    while (T-->0) {
        cin >> S;
        int n=0;
        bool p=false;
        if (S[0]=='-') n++;
        for (int i=0; i<S.length(); i++)
            if (S[i]=='+') {
                p=true;
            } else {
                if (p) n+=2;
                p=false;
            }
        cout << "Case #" << TT++ << ": " << n << endl;
    }
}