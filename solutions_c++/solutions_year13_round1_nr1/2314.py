/* This uses the GNU MP library - gmplib.org */
/* LDLIBS = -lgmpxx -lgmp */
#include <clocale>
#include <gmpxx.h>
#include <iostream>

static const mpf_class GMP_PI("0.31415926535897932384626433832795e1");

mpf_class disk_area(mpz_class radius) {
    return radius * radius * GMP_PI;
}

mpf_class ring_area(mpz_class radius) {
    return disk_area(radius + 1) - disk_area(radius);
}

int main(int argc, char **argv) {
    std::setlocale(LC_ALL, "C");

    int cases;
    std::cin >> cases;
    for (int casei = 1; casei <= cases; casei++) {
        mpz_class radius;
        mpf_class ink, ink_needed;
        std::cin >> radius >> ink;
        ink *= GMP_PI;

        long ring_count = 0;
        while ((ink_needed = ring_area(radius)) <= ink) {
            ring_count += 1;
            radius += 2;
            ink -= ink_needed;
        }
        std::cout << "Case #" << casei << ": " << ring_count << std::endl;
    }
}
