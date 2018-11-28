#include <iostream>
#include <cstdio>

using namespace std;

int T,X,R,C;

int main()
{
    freopen("in4s.txt","r",stdin);
    freopen("out4s.txt","w",stdout);
    cin >> T;
    for (int z = 1; z <= T; z++){
        cin >> X >> R >> C;
        cout << "Case #" << z << ": ";
        if (X == 1) cout << "GABRIEL\n";
        else if (X == 2){
            if ((R*C)%2 == 0) cout << "GABRIEL\n";
            else cout << "RICHARD\n";
        }else if (X == 3){
            if ((R*C)%3 != 0 || R == 1 || C == 1) cout << "RICHARD\n";
            else cout << "GABRIEL\n";
        }else if (X == 4){
            if (R < 3 || C < 3 || (R*C)%4 != 0) cout << "RICHARD\n";
            else cout << "GABRIEL\n";
        }else if (X == 5){
            
        }else if (X == 6){
            
        }else if (X > 6){
            cout << "RICHARD\n";
        }
    }
    return 0;
}

