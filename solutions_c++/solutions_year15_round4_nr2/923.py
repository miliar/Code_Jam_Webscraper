#include <cassert>
#include <iomanip>
#include <iostream>
#include <cstdio>
#include <cmath>

bool IsZero(long double x)
{
    return std::fabs(x) < 1e-10;
}

bool Equals(long double x, long double y)
{
    return IsZero(x - y);
}

long double Solve(long double x, long double r0, long double c0, long double r1, long double c1)
{
    // std::cerr << x << '\n';
    // std::cerr << r0 << ' ' << c0 << '\n';
    // std::cerr << r1 << ' ' << c1 << '\n';
    
    const long double m00 = r0;
    const long double m01 = c0 * r0;
    const long double m10 = r1;
    const long double m11 = c1 * r1;

    // std::cerr << "--\n";
    // std::cerr << m00 << ' ' << m01 << '\n';
    // std::cerr << m10 << ' ' << m11 << '\n';

    
    const auto det = m00 * m11 - m01 * m10;
    if (IsZero(det)) {
        if (Equals(x, c0) && Equals(x, c1)) {
            return 1.0 / (r0 + r1);
        }
        if (Equals(x, c0)) {
            return 1.0 / r0;
        }
        if (Equals(x, c1)) {
            return 1.0 / r1;
        }
        return -1;
    }


    const long double i00 = m11;
    const long double i01 = -m01;
    const long double i10 = -m10;
    const long double i11 = m00;

    const long double t0 = (1.0 * i00 + x * i10) / det;
    const long double t1 = (1.0 * i01 + x * i11) / det;

    if (t0 < 0 || t1 < 0) {
        return -1;
    }
    assert (Equals(t0 * r0 + t1 * r1, 1.0));
    std::cerr << (t0 * r0 * c0 + t1 * r1 * c1 - x) << '\n';
    assert (Equals(t0 * r0 * c0 + t1 * r1 * c1, x));
    
    return std::max(t0, t1);
}

int main()
{
    std::istream& istream = std::cin;
    
    int number_of_cases;
    istream >> number_of_cases;
    for (int case_no = 1; case_no <= number_of_cases; ++case_no) {
        int n;
        long double v, x;
        istream >> n >> v >> x;
        assert (n <= 2);
        long double r[2] = { 0.0, 0.0 };
        long double c[2] = { 0.0, 0.0 };
        for (int i = 0; i < n; ++i) {
            istream >> r[i] >> c[i];
        }

        double time = Solve(x, r[0] / v, c[0], r[1] / v, c[1]);
        if (time < 0) {
            printf("Case #%d: IMPOSSIBLE\n", case_no);
        } else {
            printf("Case #%d: %.8f\n", case_no, time);
        }
    }
    return 0;
}
