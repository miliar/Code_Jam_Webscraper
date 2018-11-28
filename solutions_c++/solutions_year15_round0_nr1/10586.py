//
//  Google Jam April 10th 2015
//  Problem A. Standing Ovation
//

#include <iostream>

int main() {
    freopen("in.txt" , "r" , stdin);
    freopen("out.txt" , "w" , stdout);
    
    int tests, n, needed, clapped;
    char s[1010];


    scanf("%d", &tests);
    for (int t = 1; t <= tests; t++) {
        scanf("%d %s", &n, s);

        needed = 0; // no need for additional people at the begining
        clapped = s[0] - '0'; // initially people at position 0 will clap right away

        for (int i = 1; i <= n; i++) {
            if (s[i] != '0' && clapped < i) {
                needed += (i - clapped);
                clapped += needed; // I already paid them to come
            }
            //printf("i = %d, %d clapped, %d needed, %d will clap\n", i, clapped, needed, s[i] - '0');
            
            clapped += s[i] - '0';
        }
        printf("Case #%d: %d\n", t, needed);
    }
    return 0;
}
