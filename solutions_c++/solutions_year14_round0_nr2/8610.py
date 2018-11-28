#include <iostream>
#include <vector>
#include <cassert>
#include <limits>
#include <algorithm>
#include <iomanip>

double f(double C, double F, double X)
{
    std::vector<double> reqTimes;
    size_t maxFarms = static_cast<size_t>(X) + 2;
    reqTimes.reserve(maxFarms);
    reqTimes.push_back(0);
    const double baseRate = 2.;
    while (reqTimes.size() <=  maxFarms) {
        double rate = baseRate + F * (reqTimes.size() - 1);
        double reqTime = C / rate;
        reqTimes.push_back(reqTimes.back() + reqTime);
    }
    double time = std::numeric_limits<double>::max();
    for (size_t i = 0; i < reqTimes.size(); ++i) {
        double rate = baseRate + F * i;
        double t = reqTimes[i] + X / rate;
        time = std::min(t, time);
    }
    return time;
}

int main()
{
    auto& in = std::cin;
    auto& out = std::cout;

    size_t T;
    in >> T;
    out << std::setprecision(64);

    for (size_t t = 0; t < T; ++t) {
        double C, F, X;
        in >> C >> F >> X;
        out << "Case #" << (t + 1) << ": " << f(C, F, X) << std::endl;
    }
    
    return 0;
}

