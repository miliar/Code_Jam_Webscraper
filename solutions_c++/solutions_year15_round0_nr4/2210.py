#include <iostream>

int main () {
	const std::string RICHARD_WIN = "RICHARD";
	const std::string GABRIEL_WIN = "GABRIEL";

    int T;
    std::cin >> T;

    for (int test = 1; test <= T; ++test) {
        int X;
        int R;
        int C;

        std::cin >> X >> R >> C;

        std::cout << "Case #" << test << ": ";
        if ((R*C)%X != 0 || (X+1)/2 > R || (X+1)/2 > C || (X > 2 && X%2 == 0 && std::min(R, C) == X/2)){
        	std::cout << RICHARD_WIN << std::endl;
        }
        else {
        	std::cout << GABRIEL_WIN << std::endl;
        }

    }

    return EXIT_SUCCESS;
}