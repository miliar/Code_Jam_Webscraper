#include <iostream>
#include <sstream>

using namespace std;

int main(){
    int tc;
    int t[10];
    cin >> tc;
    for(int c = 1; c <= tc; c++){
        long long N;
        cin >> N;
        for(int i = 0; i < 10; i++) t[i] = false;
        if(N == 0) cout << "Case #" << c << ": INSOMNIA" << endl;
        else{
            int coef = 1;
            while(1){
                bool done = true;
                string ch = to_string(N * coef);
                for(int i = 0; i < ch.size(); i++){
                    t[ch[i]-'0'] = true;
                }
                for(int i = 0; i < 10; i++) done &= t[i];
                if(done) break;
                coef++;
            }
            cout << "Case #" << c << ":" << " " << N*coef << endl;
        }
    }
    return 0;
}
