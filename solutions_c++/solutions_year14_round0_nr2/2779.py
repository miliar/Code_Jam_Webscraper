#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>

using namespace std;

int main(int argc, const char *argv[])
{
    ifstream ifs(argv[1]);
    int countTestCases;
    ifs >> countTestCases;

    for (int i = 0; i < countTestCases; i++) {

        double numberOfCookiesForFarm;
        double numberOfExtraCookies;
        double numberOfCookiesToWin;
        double startCookies = 2.0f;
        double totalCookies = 0.0f;
        double totalTime = 0.0f;
        double cookiesPerSecond = startCookies;

        ifs >> numberOfCookiesForFarm >> numberOfExtraCookies >> numberOfCookiesToWin;

        while (totalCookies < numberOfCookiesToWin)
        {
            double cookiesLeftToWin = numberOfCookiesToWin - totalCookies;
            double cookiesLeftToFarm = numberOfCookiesForFarm - totalCookies;

            double timeLeftToWin = cookiesLeftToWin / cookiesPerSecond;
            double timeLeftToFarm = cookiesLeftToFarm / cookiesPerSecond;

            double cookiesLeftToWinAfterFarm = numberOfCookiesToWin;
            double timeLeftToWinAfterFarm = cookiesLeftToWinAfterFarm / (cookiesPerSecond + numberOfExtraCookies);
            if (timeLeftToWin < timeLeftToFarm + timeLeftToWinAfterFarm)
            {
                cout << "Case #" << i + 1 << ": " << fixed << setprecision(7) << totalTime + timeLeftToWin << endl;
                break;
            }
            else
            {
                totalCookies = 0;
                cookiesPerSecond += numberOfExtraCookies;
                totalTime += timeLeftToFarm;
            }
        }
    }

    return 0;
}
