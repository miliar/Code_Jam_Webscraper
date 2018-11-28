#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
using namespace std;
int main(int argc, char *argv[]) {
    int t;
    scanf("%d", &t);
    for (int tat = 0; tat < t; tat++) {
        int n;
        int array[1050] = {0};
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            scanf("%d", &array[i]);
        }
        int ans1 = 0, ans2 = 0;
        // Method 1
        for (int i = 0; i < n-1; i++) {
            if (array[i] > array[i+1]) {
                ans1 += array[i]-array[i+1];
            }
        }
        // Method 2
        int mm = 0;
        for (int i = 0; i < n-1; i++) {
            int ttt = array[i] - array[i+1];
            if (ttt > mm) mm = ttt;
        }
        
        for (int i = 0; i < n-1; i++) {
            ans2 += std::min(mm, array[i]);
        }
        
        printf("Case #%d: %d %d\n", tat+1, ans1, ans2);
    }
    
    return 0;
}
