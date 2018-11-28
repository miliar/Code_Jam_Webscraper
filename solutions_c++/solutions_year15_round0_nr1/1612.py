#include <iostream>


int main()
{
    int T;
    std::cin >> T;


    for (int t = 1; t <= T; ++t) {

        long Smax;
        std::string shyness_levels;
        std::cin >> Smax >> shyness_levels;

        long standing = 0; // number of people standing already
        long friends = 0;  // number of friends invited

        // go from lowest shyness level to highest
        for (int i = 0; i <= Smax; ++i) {
            // number of people in audience with shyness level i
            long num = (long)(shyness_levels[i] - '0');

            if (num > 0 && standing < i) {
                // need to invite friends to get current level to stand up
                friends += i - standing;
                standing = i;
            }

            standing += num;
        }

        std::cout << "Case #" << t << ": " << friends << '\n';
    }

    return 0;
}
