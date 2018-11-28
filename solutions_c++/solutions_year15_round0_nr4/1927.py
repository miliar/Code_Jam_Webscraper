#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    ofstream fout("output.out");
    ifstream fin("D-small-attempt0.in");

    int numTests;
    fin >> numTests;

    for (int i = 0; i < numTests; ++i){
        int x, r, c;
        fin >> x >> r >> c;

        bool win = false;
        if(x == 1) win = true;
        else if(x == 2 && (r*c)%2 == 0) win = true;
        else if(x == 3 && (r*c)%3 == 0 && r*c != 3) win = true;
        else if(x == 4 && (r*c)%4 == 0 && r*c > 8) win = true;

        fout << "Case #" << i + 1 << ": ";
        if(win) fout << "GABRIEL" << "\n";
        else fout << "RICHARD" << "\n";
    }

    return 0;
}
