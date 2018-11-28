#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <sstream>
#include <cstring>

bool check_fair(long long x) {
    if (x < 10)
        return true;
    if (x % 10 == 0)
        return false;

    std::ostringstream out;
    out << x;
    std::string ss = out.str();
    long long lngth = ss.length();
    long long l = lngth / 2;
    //char* s = new char [ss.length() + 1];
    //std::strcpy(s, ss.c_str());
    for (long long i = 0; i < l; ++i)
        if (ss[i] != ss[lngth-1-i])
            return false;
    return true;
}

int main() {
    int t = 10000;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        long long a = 1;
        long long b = 100000000000000;
        std::cin >> a >> b;
        long long count = 0;
        for (long long numb = a; numb <= b; ++numb) {
            long long sq = std::sqrt(float(numb));
            if (numb !=  sq * sq)
                continue;
            //std::cout << numb << "\n";
            if (check_fair(sq)) {
                if (check_fair(numb))
                    count++;
            }

        }
        std::cout << "Case #" << i + 1 << ": " << count << std::endl;
        //std::cout << i << std::endl;
    }
    std::cin >> t;
    return 0;

}