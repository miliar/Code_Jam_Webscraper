#include <fstream>
#include <string>
#include <cmath>

std::ifstream INPUT;
std::ofstream OUTPUT;

void RunCase();

int main(int argc, char *argv[])
{
    std::string inFileName("test.in");
    std::string outFileName("test.out");
    if (argc == 3)
    {
        inFileName = argv[1];
        outFileName = argv[2];
    }
    INPUT.open(inFileName.c_str());
    OUTPUT.open(outFileName.c_str());
    int noCases;
    INPUT >> noCases;
    for (int i = 0; i < noCases; i++)
    {
        OUTPUT << "Case #" << i + 1 << ": ";
        RunCase();
        OUTPUT << std::endl;
    }
    INPUT.close();
    OUTPUT.close();
    return 0;
}

typedef unsigned long long ull;

void RunCase()
{
    ull r, t, y(0);
    INPUT >> r >> t;

    double a = (-2.0 * r - 1 + std::sqrt(16 * t + std::pow(2*r + 1, 2))) / 8.0;
    y = std::floor(a);
    y--;
    while ( (y+1) * (2 * r + 2 * (y + 1) - 1) <= t){
        y++ ;
    }

    OUTPUT << y;
}
