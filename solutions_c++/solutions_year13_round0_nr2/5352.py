#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstring>

using namespace std;

ifstream fin("B.in");
ofstream fout("B.out");

int T, N, M;
int L[100][100];
int rmax[100], cmax[100];

int main() {
    fin >> T;
    for(int it =1; it <=T; it++) {
        fin >> N >> M;
        memset(rmax, 0, 100);
        memset(cmax, 0, 100);
        for(int i=0; i<N; i++) {
            for(int j=0; j<M; j++) {
                fin >> L[i][j];
                cmax[j] = (cmax[j] < L[i][j])? L[i][j] : cmax[j];
                rmax[i] = (rmax[i] < L[i][j])? L[i][j] : rmax[i];
            }
        }
                
        bool possible = true;        
        for(int i=0; i< N; i++) {
            for(int j=0; j< M; j++) {
                if(L[i][j] < cmax[j] && L[i][j] < rmax[i]) {
                    possible = false;
                    break;
                }
            } 
            if(! possible) break;      
        } 
        
        string answer = possible? "YES" : "NO";
        fout << "Case #" << it << ": " << answer << endl;
        
    }
}
