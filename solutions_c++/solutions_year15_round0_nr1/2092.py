#include <iostream>
#include <string>
#include <cassert>

using namespace std;

int main(){
    unsigned t;
    cin >> t;
    for(unsigned tc = 1; tc <= t; ++tc){
        unsigned smax;
        string si;
        cin >> smax >> si;
        unsigned sadd = 0;
        unsigned salr = 0;
        assert(si.length() == smax+1);
        for(unsigned k = 0; k <= smax; ++k){
            if(salr < k){
                sadd += k-salr;
                salr = k;
            }
            salr += si[k]-'0';
        }
        cout << "Case #" << tc << ": " << sadd << endl;
    }
    return 0;
}
