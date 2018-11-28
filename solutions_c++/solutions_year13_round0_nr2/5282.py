#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

int ** a;
int n;
int m;

int test(){
    int cmax[m];
    int rmax[n];
    for (int i = 0; i < n; i++) {
        rmax[i] = a[i][0];
        for (int j = 0; j < m; j++) {
            if (a[i][j] > rmax[i]) rmax[i] = a[i][j];
        }
    }
    
    for (int i = 0; i < m; i++) {
        cmax[i] = a[0][i];
        for (int j = 0; j < n; j++) {
            if (a[j][i] > cmax[i]) cmax[i] = a[j][i];
        }
    }
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (a[i][j] < cmax[j] && a[i][j] < rmax[i]) return 0;
            if (a[i][j] < 1) return 0;
        }
    }
    return 1;
}

int main(){
    int size;
    ifstream fin;
    ofstream fout;
    fin.open("B-large.in");
    fout.open("laS_output.out");
    if (!fin.good()) return 0;
    
    fin >> size;
    if (size < 1) return 0;
    int k = 0;
    while (k < size) {
        fin >> n;
        fin >> m;
        if (n < 1 || m < 1) return 0;
        a = (int **) malloc (n * sizeof (int *));
        for (int i = 0; i < n; i++) {
            a[i] = (int *) malloc (m * sizeof(int));
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                fin >> a[i][j];
            }
        }
        int result = test();
        if (result == 1) fout << "Case #" << (k + 1) << ": " << "YES" << endl;
        if (result == 0) fout << "Case #" << (k + 1) << ": " << "NO" << endl;
        for (int i = 0; i < n; i++) {
            free(a[i]);
        }
        free(a);
        k++;
    }
    fin.close();
    fout.close();    
    return 0;
}
