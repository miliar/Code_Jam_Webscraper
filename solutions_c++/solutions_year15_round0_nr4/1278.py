#define OSW2

#include <iostream>
#include <functional>
#include <algorithm>
#include <utility>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>

using namespace std;

typedef long long ll;




int main() {
#ifdef OSW
    freopen("//Users//osw//Desktop//in.txt", "r", stdin);
#endif
#ifdef OSW2
    string file_name = "D-small-attempt2";
    freopen(("//Users//osw//Downloads//" + file_name + ".in").c_str(), "r", stdin);
    freopen(("//Users//osw//Downloads//" + file_name + ".out").c_str(), "w", stdout);
#endif
    
    int T, t = 0;
    cin >> T;

    while (T-(t++)) {
        cout << "Case #" << t << ": ";
        int a,b,c;
        cin >> a >> b >> c;
        
        if (b<c) swap(b,c);

        if (1==a) cout << "GABRIEL" << endl;
        else if (2==a) {
            if (0==b%2 || 0==c%2)   cout << "GABRIEL" << endl;
            else                    cout << "RICHARD" << endl;
        }
        else if (3==a) {
            if ((1!=b && 0==c%3)|| (1!=c && 0==b%3))    
                                    cout << "GABRIEL" << endl;
            else                    cout << "RICHARD" << endl;
        }
        else if (a==4) {
            if ((3<=b && 0==c%4)|| (3<=c && 0==b%4))    
                                    cout << "GABRIEL" << endl;
            else                    cout << "RICHARD" << endl;
        }
        else if (a==5) {
            if ((4<=b && 0==c%5)|| (4<=c && 0==b%5))    
                                    cout << "GABRIEL" << endl;
            else                    cout << "RICHARD" << endl;
        }
        else if (a==6) {
            if ((4<=b && 0==(b*c)%6)|| (4<=c && 0==(b*c)%6))    
                                    cout << "GABRIEL" << endl;
            else                    cout << "RICHARD" << endl;
        }
        else if (a>=7) cout << "RICHARD" << endl;

    }
}



