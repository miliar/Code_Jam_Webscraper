#include <fstream>
#include <vector>
#include <algorithm>

int main() {
    std::ifstream fin("D-large.in");
    std::ofstream fout("output_large.txt");
    int testCasesCount = 0;
    fin >> testCasesCount;
    for (int i = 1; i <= testCasesCount; ++i) {
        int blocksCount = 0;
        fin >> blocksCount;
        std::vector<double> naomiBlocks(blocksCount, 0);
        std::vector<double> kenBlocks(blocksCount, 0);
        for (int j = 0; j < blocksCount; ++j) {
            fin >> naomiBlocks[j];
        }
        for (int j = 0; j < blocksCount; ++j) {
            fin >> kenBlocks[j];
        }
        std::sort(naomiBlocks.begin(), naomiBlocks.end());
        std::sort(kenBlocks.begin(), kenBlocks.end());
        int deceitfulWar = 0;
        int war = 0;
        // offset - offset from begin of Naomi blocks
        int offset = 0;
        int kenRightBorder;
        int kenLeftBorder = 0;
        int looseCount = 0;
        for (kenRightBorder = blocksCount - 1; kenRightBorder >= 0 && kenBlocks[kenRightBorder] > naomiBlocks[blocksCount-1]; --kenRightBorder, ++offset);
        if (kenLeftBorder < kenRightBorder) {
            //for (kenLeftBorder = 0; kenLeftBorder < kenRightBorder && offset < blocksCount && kenBlocks[kenLeftBorder] > naomiBlocks[offset]; ++kenLeftBorder, ++offset);
            //for (int j = offset; j < blocksCount && kenLeftBorder < kenRightBorder && kenBlocks[kenLeftBorder] > naomiBlocks[j]; ++j, ++offset);
        
            for (int m = offset; m < blocksCount && kenRightBorder >= kenLeftBorder; ++m) {
                if (naomiBlocks[m] < kenBlocks[kenLeftBorder]) {
                    ++looseCount;
                    --kenRightBorder;
                }
                else {
                    ++kenLeftBorder;
                }
                //if (naomiBlocks[m] > kenBlocks[blocksCount-m-1] && naomiBlocks[m] ) {
                //    --m; // Naomi wins in this case, we just calculate how many she loose
                //    break;
                //}
            }
        }
        deceitfulWar = blocksCount - offset - looseCount;
        int k = 0; // Ken counter
        int j = 0; // Naomi counter
        /*for (j = 0; j < blocksCount && k < blocksCount; ++j) {
        for (; k < blocksCount && naomiBlocks[j] > kenBlocks[k]; ++k);
        if (k >= blocksCount) {
        break;
        }
        kenBlocks[k] = -1;
        }*/
        kenLeftBorder = 0;
        kenRightBorder = blocksCount - 1;
        looseCount = 0;
        for (j = blocksCount - 1; j >= 0; --j) {
            if (naomiBlocks[j] < kenBlocks[kenRightBorder]) {
                --kenRightBorder;
                ++looseCount;
            }
            else {
                ++kenLeftBorder;
            }
        }
        war = blocksCount - looseCount;
        fout << "Case #" << i << ": " << deceitfulWar << ' ' << war << '\n';
    }
    fin.close();
    fout.close();
    return 0;
}