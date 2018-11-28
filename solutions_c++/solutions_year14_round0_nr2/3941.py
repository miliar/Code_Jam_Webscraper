#include <fstream>
#include <iomanip>

int main()
{
    int testCasesCount = 0;
    std::ifstream fin("B-large.in");
    std::ofstream fout("output_large.txt");
    fin >> testCasesCount;
    for(int i = 1; i <= testCasesCount; ++i) {
        double c, f, x, perSecond = 2.0, currRoundTime = 0.0, totalTime = 0.0, timeToFinishCurrRate, timeToFinishNextRound;
        fin >> c >> f >> x;
        do {
            totalTime += currRoundTime;
            currRoundTime = c / perSecond;
            timeToFinishCurrRate = x / perSecond;
            perSecond += f;
            timeToFinishNextRound = currRoundTime + (x / perSecond);
        } while (timeToFinishNextRound < timeToFinishCurrRate/* || fabs(timeToFinishCurrRate - timeToFinishNextRound) <= 0.0000001*/);
        fout << "Case #" << i << ": " << std::fixed << std::setprecision(8) << totalTime + timeToFinishCurrRate << '\n';
    }
    fin.close();
    fout.close();
    return 0;
}