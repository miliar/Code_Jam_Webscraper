#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;

bool gana(char Y, string h1, string h2, string h3, string h4);
bool cuentale(string H, char Y);
bool cuentalev(vector<char> H, char Y);
bool inconcluso(string h1, string h2, string h3, string h4);

int main(int argc, char *argv[]) {

    int T;
    int caso = 0;
    char tictac1[4];
    char tictac2[4];
    char tictac3[4];
    char tictac4[4];
    int i, j;

    cin >> T;

    while(T--) {
        caso++;
        scanf("%s", tictac1);
        scanf("%s", tictac2);
        scanf("%s", tictac3);
        scanf("%s", tictac4);
        scanf("\n", NULL);
        string s1(tictac1);
        string s2(tictac2);
        string s3(tictac3);
        string s4(tictac4);
        if(gana('X', s1, s2, s3, s4)) {
            cout << "Case #" << caso << ": X won" <<endl;
        }

        else if(gana('O', s1, s2, s3, s4)) {
            cout << "Case #" << caso << ": O won" <<endl;
        }
        else if(inconcluso(s1, s2, s3, s4)) {
            cout << "Case #" << caso << ": Game has not completed" << endl;
        }
        else {
            cout << "Case #" << caso << ": Draw" << endl;
        }

    }

    return 0;
}

bool gana(char Y, string h1, string h2, string h3, string h4) {
    vector<char> v1, v2, v3, v4;

    v1.push_back(h1[0]);
    v1.push_back(h2[0]);
    v1.push_back(h3[0]);
    v1.push_back(h4[0]);

    v2.push_back(h1[1]);
    v2.push_back(h2[1]);
    v2.push_back(h3[1]);
    v2.push_back(h4[1]);

    v3.push_back(h1[2]);
    v3.push_back(h2[2]);
    v3.push_back(h3[2]);
    v3.push_back(h4[2]);

    v4.push_back(h1[3]);
    v4.push_back(h2[3]);
    v4.push_back(h3[3]);
    v4.push_back(h4[3]);

    vector<char> x1, x2;

    x1.push_back(h1[0]);
    x1.push_back(h2[1]);
    x1.push_back(h3[2]);
    x1.push_back(h4[3]);

    x2.push_back(h1[3]);
    x2.push_back(h2[2]);
    x2.push_back(h3[1]);
    x2.push_back(h4[0]);

    if(cuentale(h1, Y))
        return true;

    else if(cuentale(h2, Y))
        return true;
    else if(cuentale(h3, Y))
        return true;
    else if(cuentale(h4, Y))
        return true;

    else if(cuentalev(v1, Y))
        return true;
    else if(cuentalev(v2, Y))
        return true;
    else if(cuentalev(v3, Y))
        return true;
    else if(cuentalev(v4, Y))
        return true;

    else if(cuentalev(x1, Y))
        return true;
    else if(cuentalev(x2, Y))
        return true;
    else return false;

}

bool cuentale(string H, char Y) {
    if(count(H.begin(), H.end(), Y) >= 3) {
        if(count(H.begin(), H.end(), Y) == 4)
            return true;
        else if(count(H.begin(), H.end(), 'T') > 0)
            return true;
        else return false;
    }
    else return false;
}

bool cuentalev(vector<char> H, char Y) {
    if(count(H.begin(), H.end(), Y) >= 3) {
        if(count(H.begin(), H.end(), Y) == 4)
            return true;
        else if(count(H.begin(), H.end(), 'T') > 0)
            return true;
        else return false;
    }
    else return false;
}

bool inconcluso(string h1, string h2, string h3, string h4) {
    if(count(h1.begin(), h1.end(), '.') > 0)
        return true;
    else if(count(h2.begin(), h2.end(), '.') > 0)
        return true;
    else if(count(h3.begin(), h3.end(), '.') > 0)
        return true;
    else if(count(h4.begin(), h4.end(), '.') > 0)
        return true;
    else return false;
}

