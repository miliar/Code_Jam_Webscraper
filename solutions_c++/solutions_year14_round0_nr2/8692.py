#include <iostream>
#include <iomanip>

int main() {
    int N;
    double C;
    double F;
    double X;
    double cookies = 0;
    double seconds = 0;
    double cookies_per_sec = 2;

    std::cin >> N;

    for (int i = 0; i < N; ++i) {
        std::cin >> C >> F >> X;
        cookies = 0;
        seconds = 0;
        cookies_per_sec = 2;
        
        while (cookies < X) {

            if (cookies + C > X) {
                seconds += (X - cookies) / cookies_per_sec;
                cookies = X;
                std::cout << "Case #" << i + 1 << ": " << std::setprecision(7) << std::fixed << seconds << std::endl;
                break;
            }
            
            seconds += C / cookies_per_sec;
            cookies += C;
            
            if ( ((X - cookies) / cookies_per_sec) > (X / (cookies_per_sec + F)) ) {
                cookies = 0;
                cookies_per_sec += F;
            } else {
                seconds += (X - cookies) / cookies_per_sec;
                std::cout << "Case #" << i + 1 << ": " << std::setprecision(7) << std::fixed << seconds << std::endl;
                break;
            }
        }
    }
}
