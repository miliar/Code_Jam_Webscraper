#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

std::string input = "input.in";
std::string output = "output.out";

//#define debug(format, ...) printf(format, __VA_ARGS__)
#define debug(format, ...)

const double difference = 0.0000001;

void parseArguments(int argc, char** argv) {
    if (argc == 1) {
        return;
    }

    if (argc > 1) {
        input = argv[1];
        debug("Using custom input file: %s\n", input.c_str());
        output = input.substr(0, input.find('.')) + ".out";
        debug("Using custom output file: %s\n", output.c_str());
    }
}

int main(int argc, char** argv)
{
    parseArguments(argc, argv);

    freopen(input.c_str(), "r", stdin);
    freopen(output.c_str(), "w", stdout);

    int tc;
    cin >> tc;
    debug("N testcases = %d\n\n", tc);

    for (int test=1; test <= tc; ++test) {
        debug("Test %d\n", test);

        int N;
        cin >> N;

        vector<double> naomiDeceitful;
        vector<double> kenDeceitful;

        double aux;
        for (int i=0; i < N; ++i) {
            cin >> aux;
            naomiDeceitful.push_back(aux);
            //debug("Naomi %d block: %f\n", i, naomi.back());
        }

        for (int i=0; i < N; ++i) {
            cin >> aux;
            kenDeceitful.push_back(aux);
            //debug("Ken %d block: %f\n", i, ken.back());
        }

        sort(naomiDeceitful.begin(), naomiDeceitful.end());
        sort(kenDeceitful.begin(), kenDeceitful.end());

        for (int i=0; i < N; ++i) {
            //debug("%d sorted block: naomi %f, ken %f\n", i, naomi.at(i), ken.at(i));
        }

        vector<double> naomiWar(naomiDeceitful);
        vector<double> kenWar(kenDeceitful);

        int deceitfulPoints = 0;
        int warPoints = 0;

        double toldNaomi, chosenNaomi, chosenKen;

        // Deceitful War
        while (naomiDeceitful.size() > 0) {
            // Make Ken spend his best block in case he's min is bigger than Naomi's
            if (naomiDeceitful.front() < kenDeceitful.front()) {
                toldNaomi = kenDeceitful.back() - difference;
                chosenKen = kenDeceitful.back();
                kenDeceitful.pop_back();

                chosenNaomi = naomiDeceitful.front();
                naomiDeceitful.erase(naomiDeceitful.begin());
            } else {
                toldNaomi = kenDeceitful.back() + difference;
                chosenKen = kenDeceitful.front();
                kenDeceitful.erase(kenDeceitful.begin());

                chosenNaomi = naomiDeceitful.front();
                naomiDeceitful.erase(naomiDeceitful.begin());
            }

            if (chosenNaomi > chosenKen) {
                deceitfulPoints++;
            }
        }

        // War
        while (naomiWar.size() > 0) {
            chosenNaomi = naomiWar.back();
            naomiWar.pop_back();

            if (chosenNaomi > kenWar.back()) {
                chosenKen = kenWar.front();
                kenWar.erase(kenWar.begin());
            } else {
                for (vector<double>::iterator it=kenWar.begin(); it != kenWar.end(); ++it) {
                    if (*it > chosenNaomi) {
                        chosenKen = *it;
                        kenWar.erase(it);
                        break;
                    }
                }
            }

            if (chosenNaomi > chosenKen) {
                warPoints++;
            }
        }
        printf("Case #%d: %d %d\n", test, deceitfulPoints, warPoints);
    }

    return 0;
}

