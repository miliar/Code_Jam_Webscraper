/*
 * abeakkas
 * Google CodeJam 2016 - Round 2
 * Problem A
 * Maybe this time...
 */
#include <algorithm>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

typedef long long ll;
typedef unsigned long long ull;

// #define pr pair<ll,ll>
// #define vpr vector<pair<ll,ll> >

// Code snippets:
// (int*)calloc(1000000, sizeof(int));
// (int*)malloc(1000000 * sizeof(int));
// cout << setprecision(20);

using namespace std; 
ifstream fin("A.in");
ofstream fout("A.out");

int As[13];
int Bs[13];
int Cs[13];
string parses[3][13];

int main(){
    As[1] = 1;
    Bs[1] = 1;
    Cs[1] = 0;
    int k = 2;
    for(int i = 2; i < 13; i++) {
        As[i] = As[i - 1] + Cs[i - 1];
        Bs[i] = Bs[i - 1] + As[i - 1];
        Cs[i] = Cs[i - 1] + Bs[i - 1];
    }
    parses[0][1] = "P";
    parses[1][1] = "R";
    parses[2][1] = "S";
    for(int i = 2; i < 13; i++) {
        if(parses[0][i - 1] < parses[1][i - 1]) {
            parses[0][i] = parses[0][i - 1] + parses[1][i - 1];
        } else {
            parses[0][i] = parses[1][i - 1] + parses[0][i - 1];
        }
        if(parses[1][i - 1] < parses[2][i - 1]) {
            parses[1][i] = parses[1][i - 1] + parses[2][i - 1];
        } else {
            parses[1][i] = parses[2][i - 1] + parses[1][i - 1];
        }
        if(parses[2][i - 1] < parses[0][i - 1]) {
            parses[2][i] = parses[2][i - 1] + parses[0][i - 1];
        } else {
            parses[2][i] = parses[0][i - 1] + parses[2][i - 1];
        }
    }
    int T;
    fin >> T;
    for(int iT = 1; iT <= T; iT++) {
        fout << "Case #" << iT << ": ";
        int N, R, P, S;
        fin >> N >> R >> P >> S;
        if(As[N] == P && Bs[N] == R) {
            if(parses[0][N] < parses[1][N]) {
                fout << parses[0][N] << parses[1][N] << endl;
            } else {
                fout << parses[1][N] << parses[0][N] << endl;
            }
        } else if(Bs[N] == P && Cs[N] == R) {
            if(parses[0][N] < parses[2][N]) {
                fout << parses[0][N] << parses[2][N] << endl;
            } else {
                fout << parses[2][N] << parses[0][N] << endl;
            }
        } else if(Cs[N] == P && As[N] == R) {
            if(parses[1][N] < parses[2][N]) {
                fout << parses[1][N] << parses[2][N] << endl;
            } else {
                fout << parses[2][N] << parses[1][N] << endl;
            }
        } else {
            fout << "IMPOSSIBLE" << endl;
        }
    }
	return 0;
}
