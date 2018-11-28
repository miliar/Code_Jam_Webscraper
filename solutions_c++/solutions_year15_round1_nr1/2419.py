#include <cstdio>

int main() {
    
    int testCases;
    
    scanf("%d", &testCases);
    
    for (int testCase = 1; testCase <= testCases; ++testCase) {
        
        int n;
        int mushrooms[2000], difference, biggestDifference = 0;
        int sum1 = 0, sum2 = 0;
        
        scanf("%d", &n);
        
        scanf("%d", &mushrooms[0]);
        for (int i = 1; i < n; ++i) {
            scanf("%d", &mushrooms[i]);
            difference = mushrooms[i - 1] - mushrooms[i];
            if (difference > 0) {
                sum1 += difference;
            }
            if (biggestDifference < difference) {
                biggestDifference = difference;
            }
        }

        for (int i = 0; i < n - 1; ++i) {
            sum2 += mushrooms[i] < biggestDifference ? mushrooms[i] : biggestDifference;
        }

        printf("Case #%d: %d %d\n", testCase, sum1, sum2);
        
    }
    
    return 0;
    
}
