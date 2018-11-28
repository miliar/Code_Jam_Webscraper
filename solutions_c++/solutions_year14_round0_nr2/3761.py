#include <iostream>

double timeTo(const double rate, const double required) {
    return required / rate;
}

bool buy(const double rate, const double C, const double F, const double X) {
    double timeWithoutBuy = timeTo(rate, X);
    double timeWithBuy = timeTo(rate, C) + timeTo(rate+F,X);
    return timeWithoutBuy > timeWithBuy;
}

double solve(const double C, const double F, const double X) {
    double rate = 2.0;
    double target = X;
    double elapsed = 0.0;
    while (true) {
        if (buy(rate, C, F, target)) {
            elapsed += timeTo(rate, C);
            rate += F;
        } else {
            elapsed += timeTo(rate, target);
            break;
        }
    }
    return elapsed;
}

void solveCase(const int caseNum) {
    double C, F, X;
    std::cin >> C >> F >> X;
    std::cout << "Case #" << caseNum << ": " << solve(C, F, X) << std::endl;
}

void runTests() {
    std::cerr << "case 1 is " << solve(30, 1, 2) << " should be 1\n";
    std::cerr << "case 2 is " << solve(30, 2, 100) << " should be 39.1666667\n";
    std::cerr << "case 3 is " << solve(30.5, 3.14159, 1999.19990) << " should be 63.9680013\n";
    std::cerr << "case 4 is " << solve(500, 4, 2000) << " should be 526.1904762\n";
}

int main() {
    std::cout.precision(15);
    // runTests();
    int T;
    std::cin >> T;
    for(int i = 1; i <= T; ++i) {
        solveCase(i);
    }
}
