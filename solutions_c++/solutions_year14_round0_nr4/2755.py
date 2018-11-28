#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int countWarScore(vector<double> n, vector<double>k);
int countDWarScore(vector<double> n, vector<double>k);

int main(int argc, char * argv[]) {
    int T, c = 1, numBlocks, i;
    double block;

    scanf("%d", &T);
    while (T--) {
        vector<double> naomiWarBlocks, kenWarBlocks;
        scanf("%d", &numBlocks);
        for (i = 0; i < numBlocks; i++) {
            scanf("%lf", &block);
            naomiWarBlocks.push_back(block);
        }
        for (i = 0; i < numBlocks; i++) {
            scanf("%lf", &block);
            kenWarBlocks.push_back(block);
        }

        sort(naomiWarBlocks.begin(), naomiWarBlocks.end());
        sort(kenWarBlocks.begin(), kenWarBlocks.end());

        printf("Case #%d: %d %d\n", c++,
            countDWarScore(naomiWarBlocks, kenWarBlocks),
            countWarScore(naomiWarBlocks, kenWarBlocks));
    }
    return 0;
}

int countWarScore(vector<double> n, vector<double>k) { // O(N^2)
    int size = n.size(), result = 0;
    for (int i = 0; i < size; i++) {
        int currScore = 0;
        for (int j = 0; j < size; j++) {
            currScore += (n[j] < k[(i + j) % size]) ? 1 : 0;
        }
        result = max(result, currScore);
    }
    return size - result;
}

int countDWarScore(vector<double> n, vector<double>k) {
    int size = n.size(), result = 0;
    for (int i = 0; i < size; i++) {
        int currScore = 0;
        for (int j = 0; j < size; j++) {
            currScore += (n[j] > k[(i + j) % size]) ? 1 : 0;
        }
        result = max(result, currScore);
    }
    return result;
}