#include <iostream>
#include <fstream>
using namespace std;

fstream file;
fstream output;

int main()
{
    file.open("in.in");
    output.open("out1.txt");

    bool ans;
    int t, x, r, c;
    file >> t;
    for(int i=0; i < t; i++)
    {
        ans = 0;
        file >> x >> r >> c;
        if(x == 1) ans = 1;
        else if(x == 2)
        {
            if((r == 2) && (c == 3 || c == 1 || c == 2)) ans = 1;
            if(r == 4) ans = 1;
            if((c == 2) && (r == 3 || r == 1)) ans = 1;
            if(c == 4) ans = 1;
        }
        else if(x == 3)
        {
            if(r == 3 && (c == 3 || c == 2 || c == 4)) ans = 1;
            if(c == 3 && (r == 3 || r == 2 || r == 4)) ans = 1;
        }
        else if(x == 4)
        {
            if(c == 4 && r == 4) ans = 1;
            if(c == 3 && r == 4) ans = 1;
            if(c == 4 && r == 3) ans = 1;
        }

        if(ans) output << "Case #" << i+1 << ": GABRIEL\n";
        else output << "Case #" << i+1 << ": RICHARD\n";
    }

    return 0;
}
