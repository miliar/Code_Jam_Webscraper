#include <iostream>
#include <stdio.h>

int main() {
    int x;
    std::cin >> x;
    for(int i = 0; i < x; i++) {
        double cr = 2.0;
        double extra;
        double fact;
        double x;
        double time = 0;
        std::cin >> fact >> extra >> x;
        double now = x/cr;
        double up = fact/cr + x/(cr+extra);
        while (up < now) {
            time = time + fact/cr;
            cr = cr + extra;
            now = x/cr;
            up = fact/cr + x/(cr+extra);
        }
        time = time + now;
        std::cout << "Case #" << (i+1) << ": ";
        printf("%.9f",time);
        std::cout << std::endl;
    }
    return 0;
}
