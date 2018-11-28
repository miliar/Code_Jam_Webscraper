

#include <iostream>
#include <vector>
#include <string>
#include <set>

using namespace std;



int main(int argc, const char * argv[]) {
    int T;
    cin >> T;
    for(int tt = 1; tt <= T; ++tt){
        int i;
        cin >> i;
        int seen[10] = {0};
        int nseen = 0;
        long long v = i;
        for(int j=0; j<1000;++j){
            long long vv = v;
            while(vv > 0) {
                int d = vv % 10;
                vv /= 10;
                if(!seen[d]){
                    ++nseen;
                    seen[d] = 1;
                }
            }
            if(nseen == 10){
                cout << "Case #" << tt << ": " << v << endl;
                break;
            }
            v += i;
        }
        if(nseen < 10){
            cout << "Case #" << tt << ": INSOMNIA" << endl;
        }
    }
    return 0;
}
