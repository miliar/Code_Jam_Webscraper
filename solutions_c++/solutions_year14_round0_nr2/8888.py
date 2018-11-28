#include <fstream>
#include <algorithm>
#include <iomanip>

long double get_time(long double c, long double f, long double x, int t)
{
    long double speed = 2;
    long double time = 0;
    for (int i = 0; i < t; ++i) {
        time += c / speed;
        speed += f;
    }
    time += x / speed;
    return time;
}

void solution(long double c, long double f, long double x, int test, std::ofstream& out)
{
    int l = 0, r = 100000;
    while ((r - l) > 2) {
        int t1 = l + 1 + (r - l) / 3, t2 = r - (r - l) / 3;
        if (get_time(c, f, x, t1) > get_time(c, f, x, t2))
            l = t1;
        else
            r = t2;
    }

    out << "Case #" << test << ": " << std::setprecision(10) << std::min(get_time(c, f, x, l), 
        std::min(get_time(c, f, x, l + 1), get_time(c, f, x, r))) << std::endl;
}

int main()
{
    std::ifstream in("B-large.in");
    std::ofstream out("B-large.out");

    int test;
    in >> test;
    for (int t = 0; t < test; ++t) {
        long double c, f, x;
        in >> c >> f >> x;
        solution(c, f, x, t + 1, out);
    }
}
