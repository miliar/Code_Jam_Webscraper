#include <string>
#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

unsigned long long doit(unsigned long long r, unsigned long long t)
{
    double tmp = 2 * r - 1;
    return floor((sqrt(pow(tmp, 2) + 8 * t) - tmp) / 4.0);
}
int main (int argc, char*argv[])
{
    ifstream input("a-small-attempt0.in");
    int x = 0;
    input >> x;
    unsigned long long r, t;
    int cnt = 0;
    for (int i = 0; i < x; ++i)
    {
	cnt = 0;
	input >> r >> t;
	unsigned long long res = doit(r, t);
	cout << "Case #" << i + 1 << ": ";
	cout << res;
	cout << std::endl;
    }
}
