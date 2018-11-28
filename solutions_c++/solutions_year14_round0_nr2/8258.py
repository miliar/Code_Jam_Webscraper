#include <iostream>
#include <float.h>

using namespace std;

bool shouldBuyFarm(long double C, long double F, long double X, long double cookiesPerSecond) {
    long double timeIfBoughtFarm = C / cookiesPerSecond + X / (cookiesPerSecond + F);
    long double timeIfNoFarm = X / cookiesPerSecond;
    
    return timeIfBoughtFarm < timeIfNoFarm;
}

long double cookieGame(long double C, long double F, long double X, long double cookiesPerSecond) {
    long double timeElapsed = 0;
    while (shouldBuyFarm(C, F, X, cookiesPerSecond)) {
        timeElapsed += C / cookiesPerSecond;
        cookiesPerSecond += F;
    }
    
    timeElapsed += X / cookiesPerSecond;
    
    return timeElapsed;
}


int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        long double C, F, X;
        cin >> C;
        cin >> F;
        cin >> X;
        long double result = cookieGame(C, F, X, 2.0);
        cout << "Case #" << i << ": " << fixed << result << endl;
    }
    
}