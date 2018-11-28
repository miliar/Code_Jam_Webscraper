#include <iostream>
#include <cmath>

using namespace std;

int main () {
    int n=0, caseNumb=0, m=0, htemp=0;
    int trawnik[100][100];
    int mapa[100][100];

    cin >> caseNumb;
    for (int g=1; g<(caseNumb+1);) {
    cin >> n >> m;
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) cin >> trawnik[i][j];
    }

    for (int i=0; i<n; i++) {
        for (int j = 0; j < m; j++) mapa[i][j] = 200;
    }

    for (int i=0; i<n; i++) {
        for (int j = 0; j < m; j++){
            if (mapa[i][j]>trawnik[i][0]) mapa[i][j]=trawnik[i][0];
            if (mapa[j][i]>trawnik[0][i]) mapa[j][i]=trawnik[0][i];
        }
    }

    for (int i=0; i<n; i++) {
        for (int j = 0; j < m; j++){
            if (mapa[i][j]!=trawnik[i][j]) {
                goto n1;
            }
        }
    }

    cout << "Case #" << g << ": YES\n";
    goto endPoint;

    n1:
    for (int i=0; i<n; i++) {
        for (int j = 0; j < m; j++) {
            mapa[i][j] = 200;
        }
    }

    for (int j=0; j<m; j++) {
        htemp = 0;
        for (int t=0; t<m; t++) if (trawnik[t][j]>htemp) htemp = trawnik[t][j];
            for (int i = 0; i < n; i++){
                if (mapa[i][j]>trawnik[0][j]) mapa[i][j]=htemp;
            }
    }

    for (int i=0; i<n; i++) {
        for (int j = 0; j < m; j++){
            if (mapa[i][j]!=trawnik[i][j]) for (int t=0; t<m; t++) {mapa[i][t]=trawnik[i][0]; }
        }
    }

    for (int i=0; i<n; i++) {
        for (int j = 0; j < m; j++){
            if (mapa[i][j]!=trawnik[i][j]) {
                goto n2;
            }
        }
    }

    cout << "Case #" << g << ": YES\n";
    goto endPoint;


    n2:
    for (int i=0; i<n; i++) {
        for (int j = 0; j < m; j++) {
            mapa[i][j] = 200;
        }
    }

    for (int i=0; i<n; i++) {
	htemp = 0;
        for (int t=0; t<m; t++) if (trawnik[i][t]>htemp) htemp = trawnik[i][t];
            for (int j = 0; j < m; j++){
                if (mapa[i][j]>trawnik[i][0]) mapa[i][j]=htemp;
            }
    }

    for (int i=0; i<n; i++) {
        for (int j = 0; j < m; j++){
            if (mapa[i][j]!=trawnik[i][j]) for (int t=0; t<n; t++) {mapa[t][j]=trawnik[0][j]; }
        }
    }

    for (int i=0; i<n; i++) {
        for (int j = 0; j < m; j++){
            if (mapa[i][j]!=trawnik[i][j]) {
                cout << "Case #" << g << ": NO\n";
                goto endPoint;
            }
        }
    }

    cout << "Case #" << g << ": YES\n";
    goto endPoint;

    endPoint:
    g++;
    }

    return 0;
}
