#include <iostream>
#include <vector>
#include <stdio.h>
#include <string>
#include <stdio.h>
using namespace std;


int ans(int S_max, char* shyness) {
    int clap_count = 0;
    int friends_needed = 0;
    int shyness_level;

    for (int i = 0; i < S_max + 1; i++) {
        shyness_level = i;
        if (shyness_level > clap_count) {
            friends_needed++;
            clap_count++;
        }

        int claps = shyness[i] - '0';
        clap_count += claps;
    }
    
    return friends_needed;
}

int main() {
    int T;
    cin >> T;

    char shyness [1000];

    for (int t = 0; t < T; t++) {
        int S_max;

        scanf("%d", &S_max);
        scanf("%s", shyness);

        int n = ans(S_max, shyness);
        printf("Case #%d: %d\n", t+1, n);

    }
    

    return 0;
}
