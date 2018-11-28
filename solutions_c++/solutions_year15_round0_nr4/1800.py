#include <fstream>

using namespace std;

int T, x, r, c;

int main(){
    ifstream cin("C:\\Users\\user\\Downloads\\D-small-attempt0.in");
    ofstream cout("C:\\Users\\user\\Downloads\\oo.out");
    cin >> T; for(int t = 1; t <= T; t++){
        cout << "Case #" << t << ": ";
        cin >> x >> r >> c;
        if(x >= 7) cout << "RICHARD\n";
        else if(r*c % x != 0) cout << "RICHARD\n";
        else if(r >= x-1 and c >= x-1) cout << "GABRIEL\n";
        else cout << "RICHARD\n";
    }
    return 0;
}
