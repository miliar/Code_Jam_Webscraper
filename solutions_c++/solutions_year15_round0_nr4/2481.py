#include <cstdio>
#include <iostream>

using namespace std;
main(){

    int T, t, out, x, r, c;

    cin >> T;

    for(t=1; t<=T; t++){

        cin>> x >> r >> c;
        out = 1;

        if((r*c)%x > 0) // 3
            out *= 0;
        //else
            if(x >= 2*min(r, c) && x!=2) // 4
            out *=0;
        //else
        if (x >= 7) //1
            out *=0;
        //else
        if (x > max(r, c)) //2
            out *=0;

        if(out == 1) {
         cout<< "Case #"  << t << ": " << "GABRIEL" << endl;
        } else {
         cout<< "Case #" << t << ": " << "RICHARD" << endl;
        }

    }




    return 0;

}
