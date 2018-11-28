#include <set>
#include <iostream>
using namespace std;

int main(){
    int t; cin >> t;
    for (int i = 1; i <= t; ++i) {
        int a, b, x=0, z; cin >> a;
        set<int> s;
        for (int j = 0; j < 16; ++ j){
            int k; cin >> k;
            if (j / 4 + 1 == a) s.insert(k);
        }
        cin >> b;
        for (int j = 0; j < 16; ++ j){
            int k; cin >> k;
            if (j / 4 + 1 == b) if (s.find(k) != s.end()) { x++; z=k; }
        }
        cout << "Case #" << i << ": ";
        switch(x){
            case 0: cout << "Volunteer cheated!" << endl; break;
            case 1: cout << z << endl; break;
            default: cout << "Bad magician!" << endl;
        }
    }
    return 0;
}