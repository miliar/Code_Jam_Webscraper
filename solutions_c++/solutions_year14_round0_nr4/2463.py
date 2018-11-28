#include <cstdio>
#include <algorithm>
#include <list>
#include <vector>

using namespace std;

// given a blockMass, find the optimal choice in blocks to beat that blockMass
double findOptimalChoice(vector<double>& blocks, double blockMass) {
    double optimalMass;
    for(int i = 0; i < blocks.size(); ++i) {
        if(blocks[i] > blockMass) {
            optimalMass = blocks[i];
            blocks.erase(blocks.begin() + i);
            return optimalMass;
        }
    }
    // give smallest mass
    optimalMass = blocks[0];
    blocks.erase(blocks.begin());
    return optimalMass;
}

vector<int> solve(int N, vector<double> naomiBlocks, vector<double> kenBlocks) {
    // points for naomi
    int deceitfulWarPoint = 0;
    int warPoint = 0;
    
    // deceitful war
    vector<double> naomiBlocksClone(naomiBlocks);
    vector<double> kenBlocksClone(kenBlocks);
    for(int i = 0; i < N; ++i) {
        if(!(naomiBlocksClone[N - i - 1] < kenBlocksClone[0])) { 
            double kenMass = kenBlocksClone[i];
            double naomiMass = findOptimalChoice(naomiBlocksClone, kenMass);
            if(naomiMass > kenMass) {
                ++deceitfulWarPoint;
            }
        } else {
            break;
        }
    }


    // normal war
    for(int i = 0; i < N; ++i) {
        if(!(naomiBlocks[N - 1] < kenBlocks[0])) { 
            double naomiMass = naomiBlocks[i];
            double kenMass = findOptimalChoice(kenBlocks, naomiMass);
            if(naomiMass > kenMass) {
                ++warPoint;
            }
        } else {
            break;
        }
    }

    vector<int> result;
    result.push_back(deceitfulWarPoint);
    result.push_back(warPoint);
    return result;
}

int main() {
    int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; ++t) { 
        int N;
        scanf(" %d", &N);

        vector<double> naomiBlocks;
        for(int i = 0; i < N; ++i) {
            double mass;
            scanf(" %lf", &mass);
            naomiBlocks.push_back(mass);
        }
        sort(naomiBlocks.begin(), naomiBlocks.end());

        vector<double> kenBlocks;
        for(int i = 0; i < N; ++i) {
            double mass;
            scanf(" %lf", &mass);
            kenBlocks.push_back(mass);
        }
        sort(kenBlocks.begin(), kenBlocks.end());

        vector<int> result = solve(N, naomiBlocks, kenBlocks);
        printf("Case #%d: %d %d\n", t, result[0], result[1]);
    }

    return 0;
}
