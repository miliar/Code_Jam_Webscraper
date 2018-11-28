#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <stdint.h>

using namespace std;

void solve(int count) {
    printf("Case #%d: ", count);
    
    int numFiles, capacity;
    scanf("%d %d\n", &numFiles, &capacity);
    vector<int> fileSizes;
    for (int i = 0; i < numFiles; ++i) {
        int tmp;
        scanf("%d", &tmp);
        fileSizes.push_back(tmp);
    }
    std::sort (fileSizes.begin(), fileSizes.end());
    scanf("\n");
    
    int discs = 0;
    
    while (fileSizes.size() > 0) {
        // Find best match
        int minDelta = capacity + 1;
        int delta = 0;
        int m1 = -1, m2 = -1;
        for (int first = 0; first < fileSizes.size(); ++first) {
            int val = capacity - fileSizes[first];
            int second = fileSizes.size() - 1;
            for (; second > first; --second) {
                delta = val - fileSizes[second];
                if (delta < 0) break;
                if (delta < minDelta) {
                    minDelta = delta;
                    m1 = first; m2 = second;
                    if (minDelta == 0) {
                        break;
                    }
                }
            }
        }
        if (m1 != -1 && minDelta >= 0) {
            fileSizes.erase(fileSizes.begin() + m2);
            fileSizes.erase(fileSizes.begin() + m1);
            discs++;
        } else {
            fileSizes.erase(fileSizes.end() - 1);
            discs++;
        }
    }

    printf("%d\n", discs);
}

int main(int argc, const char * argv[]) {
	int numCases = 0;
  	scanf("%d\n", &numCases);
    
    for (int count = 1; count <= numCases; ++count) {
        solve(count);
    }
    return 0;
}

