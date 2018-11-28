#include <iostream>

using namespace std;
using ull = unsigned long long;

int main(){
    
    int T, N;
    cin >> T;
    for(int t = 1; t <= T; ++t){
        cout << "Case #" << t << ": ";
        cin >> N;
        if(N == 0){
            cout << "INSOMNIA" << endl;
        }else{
            ull n = N;
            unsigned int b = (1 << 10) - 1;
            while(1){
                int tn = n;
                //cout << tn << endl;
                while(tn){
                    int l = tn % 10;
                    b &= (~(1 << l));
                    tn /= 10;
                }
                if(!b){ cout << n << endl; break; }
                n += N;
            }
        }
    }
    
    return 0;
}