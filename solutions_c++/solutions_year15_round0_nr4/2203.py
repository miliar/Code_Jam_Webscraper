#include <fstream>
#include <iostream>

using namespace std;

int main (void)
{
    ifstream in("D.in");
    ofstream out("D.op");

    cout.rdbuf(out.rdbuf());

    int T;
    in >> T;

    for (int t = 1; t <= T; t++)
    {
        int X, R, C;
        in >> X >> R >> C;

        bool Rw = false;

        // ensure C >= R
        if (R > C)
        {
            int tmp = R;
            R = C;
            C = tmp;
        }

        if (C == 1)
        {
            if (X > 1) Rw = true;
        }

        else if (C == 2)
        {
            if (X > 2) Rw = true;
        }

        else if (C == 3)
        {
            if (R == 1)
            {
                if (X != 1) Rw = true;
            }
    
            if (R == 2)
            {
                if (X > 3) Rw = true;
            }

            if (R == 3)
            {
                if (X == 2 || X > 3) Rw = true;
            }
        }

        else if (C == 4)
        {
            if (R == 1)
            {
                if (X > 2) Rw = true;
            }

            if (R == 2)
            {
                if (X > 2) Rw = true;
            }

            if (R == 3)
            {
                
            }

            if (R == 4)
            {
                if (X == 3) Rw = true;
            }
        }

        if (C*R % X != 0) Rw = true;

        cout << "Case #" << t << ": ";
        if (Rw) cout << "RICHARD" << endl;
        else cout << "GABRIEL" << endl;
        

    }    

    return 0;
}
