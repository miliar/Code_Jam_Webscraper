#include <iostream>
#include <fstream>

class Bullseye{
public:
    Bullseye(long radius, long millilitres);
    ~Bullseye();
    long cal();

private:
    long r;
    long t;
};

Bullseye::Bullseye(long radius, long millilitres)
{
    r = radius;
    t = millilitres;
}

Bullseye::~Bullseye()
{
}

long Bullseye::cal()
{
    int count = 1;
    int tmp = 2 * r + 1;
    t =t - tmp;
    tmp = tmp + 4;
    while ( t >= tmp) {
        t = t - tmp;
        count++;
        tmp =tmp + 4;
    }
    return count;
}

int main()
{
    std::ifstream inf("A-small-attempt0.in");
    std::ofstream of("result.out");
    long T;
    inf >> T;
    long S = T;
    while (T > 0) {
        of<< "Case #" << S - T + 1 << ": ";
        long r,t;
        inf >> r >> t;
        Bullseye be(r, t);
        of << be.cal() << std::endl;
        T--;
    }

    inf.close();
    of.close();

    return 0;
}
