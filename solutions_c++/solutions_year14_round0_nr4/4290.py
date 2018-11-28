#include <iostream>
#include <string>
#include <set>
#include <sstream>
#include <iomanip>
#include <vector>
#include <algorithm>

using namespace std;

string tos(double q, int d=7) {
  stringstream A;
  A<<fixed<<setprecision(d)<<q; 
  string s; 
  A >> s; 
  return s; 
}

void solve(int ind) {
    // input
    int N;
    cin >> N;
    vector<double> naomi(N), ken(N);
    for (int i = 0; i < N; ++i) {
        cin >> naomi[i];
    }
    for (int i = 0; i < N; ++i) {
        cin >> ken[i];
    }
    sort(naomi.begin(), naomi.end());
    sort(ken.begin(), ken.end());
/*    for (int i = 0; i < N; ++i) {
        cout << naomi[i] << " ";
    }
    cout << endl;
    for (int i = 0; i < N; ++i) {
        cout << ken[i] << " ";
    }
    cout << endl;*/
    // ken strategy: always get smallest that is greater than naomi, if impossible, get smallest
    // for War:
    // naomi starts with her larger ones - does it matter?
    int nW = 0, i = N - 1;
    int kenmin = 0, kenmax = N - 1;
    while (i >= 0) {
//        cout << naomi[i] << " : ";
        // detect ken's response
        if (ken[kenmax] > naomi[i]) {
            --kenmax;
        } else {
            ++kenmin;
            ++nW;
        }
        --i;
    }
    
    // for Deceitful War:
    // naomi uses her smallest ones to take out Ken's larger ones
/*    int nDec = 0, i = 0;
    while (i < N && naomi[i] < ken[N - i - 1]) {
        cout << naomi[i] << " " << ken[N - i - 1] << endl;
        ++i;
    }
    nDec = N - i;*/
    
    // naomi finds the smallest of her blocks that can be used to kick smallest ken's
    // and sais it's incredibly large, so that he has to use the smallest one
    int nDec = 0;
    i = 0;
    while (i < N) {
        if (naomi[i] > ken[nDec]) {
//            cout << naomi[i] << " " << ken[nDec] << endl;
            ++nDec;
        }
        ++i;
    }
    
    // output
    cout << "Case #" << ind << ": " << nDec << " " << nW << endl;
}

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        solve(i);
    }
}