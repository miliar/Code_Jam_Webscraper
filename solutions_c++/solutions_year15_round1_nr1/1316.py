#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;


int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int T;
    scanf("%d", &T);
    
    for (int qq = 1; qq <= T; qq++) {
        printf("Case #%d: ", qq);
        
        int N;
        scanf("%d", &N);
        
        
        vector<int>v;
        int n;
        for (int i = 0; i < N; i++) {
            scanf("%d", &n);
            v.push_back(n);
        }
        
        int first, second, max_diff;
        first = second = max_diff = 0;
        
        for (int i = 1; i < v.size(); i++) {
            if (v[i-1] > v[i]) first += v[i-1] - v[i];
            max_diff = max(max_diff, v[i-1] - v[i]);
        }
        
        for (int i = 0; i < N - 1; i++) {
            second += min(max_diff, v[i]);
        }
        
        printf("%d %d\n", first, second);
    }
    
    return 0;
}
