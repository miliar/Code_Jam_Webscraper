#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    freopen("b-large.in","r",stdin);
    freopen("b-large.out","w",stdout);
    int T;
    cin >> T;
    for ( int a = 1; a <=T; a++ ){
        
        double c=2;
        double C;
        double F;
        double X;
        double ts=0;
        double tc=0;
        double cookies;
        cin >> C >> F >> X;
        while ( true ){
              double sec = X/c;
              double sec2 = X/(c+F);
              double fSec = C/c;
              if ( fSec+sec2 < sec ){
                 tc = 0;
                 c+=F;
                 ts += fSec;
                 continue;
              }
              
              ts += sec;
              if ( ts*c >= X ){
                break;
              }
        }
        cout << "Case #" << a << ": ";
        cout << setprecision(7) << ts << endl;
    }
    return 0;   
}
