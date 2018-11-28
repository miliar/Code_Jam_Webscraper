#include <cstdio>
#include <iostream>

/*
 * Files are assigned to stdin and stdout,
 * which allows for console level interaction.
 * Great for debugging.
 */

int main(int argc, char* argv[]) {
    //variables
    int T; // cases 1 ≤ T ≤ 100
    int Smax; //max shyness    0 ≤ Smax ≤ 6 or 0 ≤ Smax ≤ 1000
    int ovation;
    int friends;


    //selecting and opening files
    if (argc > 3 || argc == 1) {
        std::cout << "Usage is <inputFile> [<outputFile>]\n";
        return 1;
    }

    freopen(argv[1], "r", stdin);

    if (argc == 3) {
        freopen(argv[2], "w", stdout);
    } else {
        freopen("a.out", "w", stdout);
    }

    //Start getting input
    std::cin >> T;

    for (int countT = 1; countT <= T; countT++) {
std::cerr << "****** Case # is  : " << countT << " ******\n";
        friends = 0;
        ovation = 0;
        //handle input
        std::cin >> Smax;
        char S[Smax];
        std::cin >> S;
        //process data

        for (int k = 1; k <= Smax; k++) {
            ovation += S[k-1] - 48;
std::cerr << "ovation/k is  : " << ovation << "\\" << k << "\n";
            if (ovation < k) {
                friends++;
                ovation++;
std::cerr << "friend added\n";
            }
        }

        //handle output
        std::cout << "Case #" << (countT) << ": " << friends << "\n";
    }

}