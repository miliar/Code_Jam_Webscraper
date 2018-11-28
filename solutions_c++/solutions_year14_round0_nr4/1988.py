#include<iostream>
#include<algorithm>
#include<fstream>
using namespace std;
int t, i, j, k, n, war, dwar;
double naomi[2000];
double kent[2000];
bool kent_log[2000];
int main() {
    ifstream fin;
    ofstream fout;
    fin.open("D-large.in");
    fout.open("D-small-practice.out");
    fin >> t;
    for (k = 0; k < t; ++k) {
        fin >> n;
        for (i = 0; i < n; ++i) fin >> naomi[i];
        for (i = 0; i < n; ++i) {
            fin >> kent[i];
            kent_log[i] = true;
        }
        sort(naomi, naomi+n);
        sort(kent, kent+n);
        war = 0;
        dwar = 0;
        //WAR
        for (i = 0; i < n; ++i) {
            for (j = 0; j < n; ++j) {
                if ((kent[j] > naomi[i]) && (kent_log[j])) {
                    kent_log[j] = false;
                    break;
                }
            }
            if (j == n) {
                war++;
                for (j = 0; j < n; ++j) {
                    if (kent_log[j]) kent_log[j] = false;
                    break;
                }
            }
            //cout << naomi[i] << " "<< kent[i] << endl;
        }
        //DWAR
        //cout << endl;
        for (i = 0; i < n; ++i) kent_log[i] = true;
        for (i = 0; i < n; ++i) {
            for (j = 0; j < n; ++j) {
                if ((naomi[i] > kent[j]) && kent_log[j]) {
                    kent_log[j] = false;
                    dwar++;
                    break;
                }
            }
            if (j == n) {
                for (j = n-1; j > -1; --j)
                    if (kent_log[j]) {
                        kent_log[j] = false;
                        break;
                    }
            }
           // cout << naomi[i] << " "<< kent[n-1-i] << endl;
        }
        fout << "Case #" << k + 1 << ": " << dwar << " " << war << endl;
        //cout << endl;
    }
    fin.close();
    fout.close();
    return 0;
}

