#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;


int main(){
    int NN;
    cin >> NN;
    for(int nn = 1; nn <= NN; nn++){
        string s;
        cin >> s;
        int tt = s.size();
        while(tt > 0 && s[tt-1] == '+'){
            tt--;
        }
        s = s.substr(0, tt);
        
        if(s.empty()) {
            cout << "Case #" << nn << ": " << 0 << endl;
            continue;
        }
        
        
        
        char frt = s[0];
        int rev = 1;
        for(auto c: s){
            if(c != frt){
                frt = c;
                rev++;
            }
        }
        cout << "Case #" << nn << ": " << rev << endl;
    }
    return 0;
}