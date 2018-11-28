#include <iostream>
#include <cmath>

using namespace std;



int main() {

    int nbTest;

    cin >> nbTest;

    for(int i = 0; i < nbTest; ++i){
        int j,k, e;
        cin >> j >> k >> e;

        int tab[j+k];
        for(int l = 0; l < j+k; l++){
            tab[l] = l%j;
        }
        cout << "Case #" << i+1 << ": ";
        if( ceil((double) j/(double)k) > (double)e ) cout << "IMPOSSIBLE" << endl;
        else{
            for(int h = 0; (double)h < ceil((double)j/(double)k); ++h){
                unsigned long long result = 0;
                unsigned long long pow = 1;
                for(int o = 0; o < k; ++o){
                    result += tab[(h+1)*k-o]*pow;
                    pow *= j;
                }
                cout << result+1 << " ";
            }
        }
        cout << endl;

    }

    return 0;
}