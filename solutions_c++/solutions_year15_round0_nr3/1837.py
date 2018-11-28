#include <algorithm>
#include <cassert>
#include <cmath>
#include <numeric>
#include <iostream>
#include <vector>

struct Quaternion {
    double x, i, j, k;
};

inline Quaternion Mult(const Quaternion& left, const Quaternion& right) {
    return Quaternion{
        left.x * right.x - left.i * right.i - left.j * right.j - left.k * right.k,
        left.x * right.i + left.i * right.x + left.j * right.k - left.k * right.j,
        left.x * right.j - left.i * right.k + left.j * right.x + left.k * right.i,
        left.x * right.k + left.i * right.j - left.j * right.i + left.k * right.x
    };
}

bool Eq(const Quaternion& left, const Quaternion& right, double eps = 1e-8) {
    return
        std::fabs(left.x - right.x) < eps &&
        std::fabs(left.i - right.i) < eps &&
        std::fabs(left.j - right.j) < eps &&
        std::fabs(left.k - right.k) < eps;
}

constexpr Quaternion Q1{1, 0, 0, 0};
constexpr Quaternion I{0, 1, 0, 0};
constexpr Quaternion J{0, 0, 1, 0};
constexpr Quaternion K{0, 0, 0, 1};

Quaternion Power(Quaternion left, size_t power) {
    auto result = Q1;
    for (; power > 0; power >>= 1) {
        if (power & 1) {
            result = Mult(result, left);
        }
        left = Mult(left, left);
    }
    return result;
}

std::vector<Quaternion> ReadQuaternionString(std::istream* istream = &std::cin) {
    std::string string;
    *istream >> string;
    std::vector<Quaternion> result;
    result.reserve(string.size());
    for (char c : string) {
        switch (c) {
        case 'i': result.push_back(I); break;
        case 'j': result.push_back(J); break;
        case 'k': result.push_back(K); break;
        default: assert (false);
        }
    }
    return result;
}


size_t findPrefix(const std::vector<Quaternion>& string, const Quaternion& expectedMultValue) {
    size_t result = 0;
    Quaternion value = Q1;
    for (const auto& q : string) {
        ++result;
        value = Mult(value, q);
        if (Eq(value, expectedMultValue)) {
            return result;
        }
    }
    return 0;
}


size_t findSuffix(const std::vector<Quaternion>& string, const Quaternion& expectedMultValue) {
    Quaternion value = Q1;
    for (size_t i = 0; i < string.size(); ++i) {
        value = Mult(string.rbegin()[i], value);
        if (Eq(value, expectedMultValue)) {
            return i + 1;
        }
    }
    return 0;
}


template <class T>
std::vector<T> Times(const std::vector<T>& input, size_t rep) {
    std::vector<T> result;
    result.reserve(input.size() * rep);
    while (rep > 0) {
        result.insert(result.end(), input.begin(), input.end());
        --rep;
    }
    return result;
}


void Print(const Quaternion& quat) {
    std::cout << '[' << quat.x << ',' << quat.i << ',' << quat.j << ',' << quat.k << ']' << '\n';
}

bool IsIJK(const std::vector<Quaternion>& string, size_t rep) {
    { // Power(string, rep) == I * J * K
        const auto stringVal = std::accumulate(string.begin(), string.end(), Q1, Mult);
        if (!Eq(Power(stringVal, rep), Mult(I, Mult(J, K)))) {
            return false;
        }
    }
    const auto stringTimes = Times(string, 4);
    const size_t i = findPrefix(stringTimes, I);
    const size_t k = findSuffix(stringTimes, K);
    return i > 0 && k > 0 && i + k < string.size() * rep;
}


int main() {
    int number_of_cases;
    std::cin >> number_of_cases;

    for (int case_no = 0; case_no < number_of_cases; ++case_no) {
        size_t _, rep;
        std::cin >> _ >> rep;
        const auto string = ReadQuaternionString();

        std::cout << "Case #" << (case_no + 1) << ": " << (IsIJK(string, rep) ? "YES\n" : "NO\n");
    }
    return 0;
}
