/* Tomasz [Tommalla] Zakrzewski, Google Code Jam 2015
 * Qualification Round: Problem A. Standing Ovation
 */
#include <cstdio>


char audience[2000];


int main() {
        int t;
        int n;
        scanf("%d", &t);
        for (int c = 1; c <= t; ++c) {
            scanf("%d%s", &n, audience);
            int res = 0;
            int stood = 0;
            for (int s = 0; s <= n; ++s) {
                if (stood < s) {
                    res += s - stood;
                    stood = s;
                }
                
                stood += audience[s] - '0';
            }
            
            printf("Case #%d: %d\n", c, res); 
        }
        
        return 0;
}