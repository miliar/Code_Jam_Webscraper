#include <fstream>
#include <vector>
#include <string>

int main()
{
    std::ifstream in("A-small-attempt2.in");
    //std::ifstream in("input.txt");
    std::ofstream out("output.txt");

    int numTests, n;
    in >> numTests;
    for (int i = 1 ; i <= numTests; ++i) {
        in >> n;
        int numOps = 0;
        std::vector<std::string> str(n);
        for (int j = 0; j < n; ++j) {
            in >> str[j];
        }
        std::vector<int> similarCharCount(n, 0);
        std::vector<int> curPos(n, 0);
        bool FeglaWon = false;
        while (curPos[0] < str[0].size()) {
            char charInPos = str[0][curPos[0]];
            bool needBreak = false;
            int avg = 0;
            for (int j = 0; j < n; ++j) {
                int tmpPos = curPos[j];
                while (tmpPos < str[j].size() && str[j][tmpPos] == charInPos) {
                    ++avg;
                    ++similarCharCount[j];
                    ++tmpPos;
                }
                if (similarCharCount[j] == 0) {
                    FeglaWon = true;
                    break;
                }
                curPos[j] += similarCharCount[j];
            }
            if (FeglaWon) {
                break;
            }
            avg /= n;
            for (int j = 0; j < n; ++j) {
                numOps += abs(similarCharCount[j] - avg);
                similarCharCount[j] = 0;
            }
        }
        for (int j = 0; !FeglaWon && j < n; ++j) {
            if (curPos[j] < str[j].size()) {
                FeglaWon = true;
            }
        }
        if (FeglaWon) {
            out << "Case #" << i << ": Fegla Won\n";
            continue;
        }
        out << "Case #" << i << ": " << numOps << "\n";
    }
    in.close();
    out.close();
    return 0;
}