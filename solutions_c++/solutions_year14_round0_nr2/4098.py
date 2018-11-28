#include <iostream>
#include <iomanip>
#include <stdio.h>
using namespace std;

int main(){
    freopen ("in.txt", "r", stdin); freopen ("out.txt", "w", stdout);
    double n, actualProd, farmCost, farmProd, fin, totalTime;
    cin >> n;

    for (int i = 0; i < n; i++){
        actualProd = 2, totalTime=0;
        cin >> farmCost >> farmProd >> fin;
        while (farmCost/actualProd+fin/(actualProd+farmProd)<fin/actualProd){
            totalTime+=farmCost/actualProd;
            actualProd+=farmProd;
        }
        totalTime+=fin/actualProd;
        cout << "Case #" << i+1 << ": ";
        cout << fixed << setprecision(7) << totalTime << endl;
    }

    return 0;
}
