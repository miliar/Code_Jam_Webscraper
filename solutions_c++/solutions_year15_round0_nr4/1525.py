#include <iostream>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

const int richard = 0; // exist figure cannot win
const int gabriel = 1;

int test()
{
    int x, r, c;
    scanf("%d%d%d", &x, &r, &c);
    if (r < c)
        swap(r, c);
    int sq = r * c;
    if (sq % x != 0)
        return richard;
        
    if (x == 1)
    {
        return gabriel;
    }
    if (x == 2)
    {
        return gabriel;
    }
    if (x == 3)
    {
        if (r == 3 && c == 1)
            return richard;
        return gabriel;
    }
    if (x == 4)
    {
        if (r < 4)
            return richard;
        if (r == 4)
        {
            if (c <= 2)
                return richard;
            if (c == 3)
                return gabriel;
            if (c == 4)
                return gabriel;
        }
    }
}

int main()
{
    freopen("d-small-attempt1.in", "r", stdin);
    freopen("d_out.txt", "w", stdout);
    
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++)
    {
        cout << "Case #" << i + 1 << ": " << (test() == richard ? "RICHARD" : "GABRIEL") << endl;
    }
    return 0;
}
