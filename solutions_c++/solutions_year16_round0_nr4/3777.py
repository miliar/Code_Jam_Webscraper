#include <iostream>
using namespace std;
int f(int w){

}
int main() {
    int nn; 
    cin >> nn;
    for (int i = 1; i<=nn; i++) {
        cout << "Case #"<<i<<": ";
        int k , c, s;
        cin >> k >> c >> s;
        if (k==s) {
            for (int t0=1; t0<=k; t0++) {
                unsigned long long t = t0;
                for (int w = 2; w<=c; w++)
                    t = (t-1)*k+t0;
                cout << t;
                if (t0==k) cout << endl; else cout <<" ";
            }
        }
        else cout << endl;
    }
    

    
}
