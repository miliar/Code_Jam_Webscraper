#include <iostream>

int main() {
    int T, cookies, factoryNum;
    double C, F, X, answer;
    double sec, nextSec, cookiesPerSec, nextCookiesPerSec, total, next, wait;

    std::cin >> T;
    for (int i=0; i < T; ++i) {
        std::cin >> C >> F >> X;
        factoryNum = 0;
        total = 0;

        cookiesPerSec = 2.0 + factoryNum*F;
        nextCookiesPerSec = 2.0 + (factoryNum+1)*F;
        sec = X / cookiesPerSec;
        nextSec = X / nextCookiesPerSec;

        while (sec - nextSec > C / cookiesPerSec) { // true => buy another factory
            ++factoryNum;
            total += C / cookiesPerSec;

            cookiesPerSec = 2.0 + factoryNum*F;
            nextCookiesPerSec = 2.0 + (factoryNum+1)*F;
            sec = X / cookiesPerSec;
            nextSec = X / nextCookiesPerSec;
            
            //std::cout << total << " " << sec << " " << cookiesPerSec << std::endl;
        }

        // wait until X
        wait = X / cookiesPerSec;

        printf("Case #%d: %.7lf\n", i+1, total + wait);
    }

    return 0;
}
