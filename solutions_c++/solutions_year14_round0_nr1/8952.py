#include <stdio.h>
#include <cmath>
#include <algorithm>
#include <map>
#include <utility>
#include <set>
#include <vector>
#include <string.h>
#include <queue>
#include <iostream>
#include <stdlib.h>

using namespace std;

#define MAXN 1000005
#define MOD 1000000007
#define INF (1 << 30)
#define st first
#define nd second

int matriz[4][4],matriz2[4][4];
int A, B;

int main() {
    int T;
    cin >> T;
    for(int i = 1; i <= T; i++){
        cin >> A;
        A--;
        for(int j = 0; j < 4; j++)
            for(int k = 0; k < 4; k++)
                cin >> matriz[j][k];
        cin >> B;
        B--;
        for(int j = 0; j < 4; j++)
            for(int k = 0; k < 4; k++)
                cin >> matriz2[j][k];
        int cont = 0, valor;
        for(int j = 0; j < 4; j++)
            for(int k = 0; k < 4; k++)
                if(matriz[A][j] == matriz2[B][k])
                    cont++, valor = matriz[A][j];
        cout << "Case #" << i << ": ";
        if(cont == 1)
            cout << valor;
        else if(cont == 0)
            cout << "Volunteer cheated!";
        else cout << "Bad magician!";
        cout << endl;
    }
    return 0;
}
