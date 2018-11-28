#include <iostream>
#include <vector>
#include <cassert>
using namespace std;
int t;
int used = 0;
int xom, r, c;

void solve(int t)
{   
    cin >> xom >> r >> c;
    used = 0;
    bool rich = false;
    if (r > c)
        swap(r, c);
    if (xom == 1)
    {
        // gabr
    }
    else if (xom == 2)
    {
        if (r * c % 2 == 1)
            rich = true;
    }
    else if (xom == 3)
    {
        if (r == 1)
        {
            rich = true;
        }
        else if (r == 2)
        {
            rich = (c == 2) || (c == 4);
        }
        else if (r == 3)
        {
            // gab
        }
        else
            rich = true;
    }
    else
    {
        if (r != 4)
        {
            rich = true;
        } 
        if (r == 3 && c == 4)
            rich = false;
    }
    cout << "Case #" << t << ": " << (rich ? "RICHARD" : "GABRIEL") << endl;
}

int main()
{
    cin >> t;
    for(int i = 1; i <= t; ++i)
        solve(i);
}
