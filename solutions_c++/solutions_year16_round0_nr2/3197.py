#include <bits/stdc++.h>

#define cin fin
#define cout fout

using namespace std;

ifstream fin("B-large.in");
ofstream fout("B-large.out");

int T;
string S;

int value() {
    char mi = '-';
    int retVal=0;

    for (int i=S.size()-1; i>=0; i--) {
        if (S[i] == mi) {
            retVal ++;
            mi = (mi == '-' ? '+' : '-');
        }
    }

    return retVal;
}

int main()
{
    cin >> T;

    for (int t=1; t<=T; t++) {
        cin >> S;
        cout << "Case #" << t << ": ";
        cout << value() << endl;
    }

    return 0;
}
