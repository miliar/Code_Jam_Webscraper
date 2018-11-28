#include <iostream>
#include <iomanip>
using namespace std;
typedef long double ld;
#define X 100000

int main() {
    int t; cin>>t;
    for(int ti=1;ti<=t;++ti) {
        ld c,f,x; 
        cin>>c>>f>>x;
        
        ld m = 2;
        ld total = 0.0;
        for(int i=0; i<X;++i) {
            // buy if X/(2+i*f) > C/(2+i*f) + X/(2+(i+1)*f)
            // m = 2+i*f
            if(x* (m+f) > c*(m+f) + x*m) {
                //cerr << x*(m+f) << endl;
                total += c/m;
                m += f;
            }else{
                total += x/m;
                break;
            }
        }
        cout <<"Case #" << ti <<": ";
        cout << fixed << setprecision(7) << total << endl;
    }
    return 0;
}
