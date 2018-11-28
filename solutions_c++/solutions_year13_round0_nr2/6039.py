#include <iostream>
#include <cstdio>

using namespace std;

void algo() {
    int i, j, k, pos = 1;
    int h=0;
    static int caseNo = 0;
    int m, n, mx = 0, mn = 101;
    cin >> n >> m;
    const int n1 = n;
    const int m1 = m;
    int l[10][10];

    for (i=0; i < n; i++)
        for(j=0; j < m; j++) {
            cin >> l[i][j] ;
            if(mx < l[i][j])
                mx = l[i][j];
            //if(mn > l[i][j])   mn = l[i][j];

        }

    if(n == 1 or m == 1){
        cout << "Case #" << ++caseNo <<": "<< "YES" << endl;
        //free l;
        return;
    }

    int rowOK = 1, colOK = 1;
    int rowCkd[10],  colCkd[10];
    for(i=0; i < n; i++) {
        for(j=0; j < m; j++) {
            rowOK = 1;
            colOK = 1;
            if( l[i][j] != mx ) {

                for(k=0; k < m; k++)
                    if(l[i][j] != l[i][k]) {
                        rowOK = 0;
                        break;
                    }
                if( l[i][j] != mx ) {

                    for(k=0; k < n; k++)
                        if(l[k][j] != l[i][j]) {
                            colOK = 0;
                            break;
                        }
                }

                if(!(rowOK || colOK) ){
                    cout << "Case #" << ++caseNo <<": "<< "NO" << endl;
                    return;
                }
            }


        }
    }

    cout << "Case #" << ++caseNo <<": "<< "YES" << endl;


}

int main() {

    int nCases;
    cin >> nCases;
    for(int i=0; i < nCases; i++)
        algo();
    return 0;
}
