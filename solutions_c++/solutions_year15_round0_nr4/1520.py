#include <cstdlib>
#include <iostream>
#include "set"
#include <math.h>

using namespace std;

int main(int argc, char *argv[])
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T;
    cin >> T;

	int X,R,C;
	bool y;
	int xx;
    for (int T_i=0; T_i<T;T_i++){
        cin >> X >> R >> C;
        
        if (R>C) {
                 xx = R;
                 R = C;
                 C = xx;
                 }
                 
        if  (((R*C) % X) != 0) {
            y = false;} 
        else {
             if (X==1) y = ((C>=X) && (R>= ceil((float)X / 2)));
             if (X==2) y = ((C>=X) && (R>= ceil((float)X / 2)));
             if (X==3) y = ((C>=X) && (R>= ceil((float)X / 2)));
             if (X==4) y = ((C>=X) && (R>= 3));
             }
        
        if (y==false) {
        cout << "Case #" << T_i+1 << ": RICHARD" << endl;
        } else {
        cout << "Case #" << T_i+1 << ": GABRIEL" << endl;
        }
    }
    return EXIT_SUCCESS;
}
