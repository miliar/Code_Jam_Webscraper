#include<iostream>
#include<fstream>
#include<string>
#include<math.h>
using namespace std;
int i, j, k, n, t, maxx, x, result;
char temp;
string s[200];
char sc[200][200];
int sn[200][200];
int a[200];
bool check;
int main() {
    ifstream fin;
    ofstream fout;
    fin.open("A-small-attempt0.in");
    fout.open("A-small-practice.out");
    fin >> t;
    for (k = 0; k < t; ++k) {
        fin >> n;
        maxx = 0;
        for (i = 0; i < n; ++i) {
            fin >> s[i];
            x = 0;
            sc[i][0] = s[i][0];
            sn[i][0] = 1;
            for (j = 1; j < s[i].length(); ++j) {
                if (s[i][j] == s[i][j-1]) {
                    sn[i][x]++;
                }
                else {
                    x++;
                    sc[i][x] = s[i][j];
                    sn[i][x] = 1;
                }
            }
            a[i] = x;
            if ((maxx == 0) || (maxx == x)) {
                check = true;
                maxx = x;
            }
            else {
                check = false;
                break;
            }
        }
        if (!check) fout << "Case #" << k + 1 << ": " << "Fegla Won";
        else {
            fout << "Case #" << k + 1 << ": ";
            result = 0;
            for (i = 0; i <= maxx; ++i) {
                x = sn[0][i];
                for (j = 1; j < n; ++j) {
                    if (sc[j][i] != sc[j-1][i]) {
                        check = false;
                        break;
                    }
                    else x += sn[j][i];
                }
                if (!check) break;
                int balance = x/n;
                cout << k+1 << " " << maxx << " " << i << " " << x << " " << n << endl;
                for (j = 0; j < n; ++j) {
                    result += abs(balance - sn[j][i]);
                }
            }
            if (!check) fout << "Fegla Won";
            else fout << result;
        }
        fout << endl;
    }
    fin.close();
    fout.close();
    return 0;
}
