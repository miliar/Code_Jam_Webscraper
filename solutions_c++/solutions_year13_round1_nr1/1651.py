#include <iostream>

/*scratch buffer

std::cout << "Case #" << i + 1 << ": ";





*/

int szRing(int radin, int radout)
{
    return radout * radout - radin * radin;
}


int nRings(int rad,int paint)
{
    int rings = 0;
    while(szRing(rad, rad + 1) <= paint)
    {
        paint -= szRing(rad, rad+1);
        rings++;
        rad += 2;
    }
    return rings;
}

int main()
{
    int ncases = 0;
    std::cin >> ncases; 

    for(int i = 0; i < ncases; i++)
    {
        int r;
        int t;
        std::cin >> r >> t;
        std::cout << "Case #" << i + 1 << ": ";
        std::cout << nRings(r,t) << '\n';
    }
}