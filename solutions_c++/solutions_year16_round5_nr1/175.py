#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

char s[20001];

int main() {
    int t, i;
    
    scanf("%d", &t);
    
    for (i = 0; i < t; i++) {
        int n, ans = 0, j;
        vector <int> v;
        
        scanf("%s", s);
        
        n = strlen(s);
        
        for (j = 0; j < n; j++) {
            int x = 0;
            
            if (s[j] == 'C') x = 1;
            
            if (v.size() > 0 && v.back() == x) {
                v.pop_back();
                
                ans += 10;
            } else {
                v.push_back(x);
            }
        }
        
        ans += v.size() / 2 * 5;
        
        printf("Case #%d: %d\n", i + 1, ans);
    }
    
    return 0;
}
