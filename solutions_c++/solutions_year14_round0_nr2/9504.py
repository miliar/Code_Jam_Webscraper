#include <iostream>
#include <fstream>

double C, F, X;
static const int maxDepth = 100000;

double choise(double cps, double curTime, double tNoBuy, int depth)
{
    double t1 = 1.0 / 0.0, t2;
    if(curTime < tNoBuy && depth < maxDepth)
        t1 = choise(cps + F, curTime + C / cps, curTime + X / cps, depth + 1);
    t2 = curTime + X / cps;
    return t1 < t2 ? t1 : t2;
}

int main(int argc, char **argv)
{
    std::ifstream inf("cookie.in.txt");
    std::ofstream outf("cookie.out.txt");
    
    outf.precision(7);
    outf.setf( std::ios::fixed, std:: ios::floatfield );
    
    int testCount;
    inf >> testCount;
    
    for(int i = 0; i < testCount; i++)
    {
        inf >> C >> F >> X;
	outf << "Case #" << i + 1 << ": " << choise(2.0, 0.0, X / 2.0, 1) << std::endl;
    }
    
    inf.close();
    outf.close();
    
    return 0;
}
