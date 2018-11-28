#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cstdlib>

using namespace std;

int main() {
    int tc;
    scanf("%d", &tc);
    for(int i = 0; i < tc; i++) {
        int max;
        scanf("%d", &max);
        char s [1005];
        scanf("%s", s);
        int len = strlen(s);
        int current = 0;
        int needed = 0;
        //printf("Read this -> %s \n", s);
        for(int j = 0; j < len; j++) {
           if(s[j] - '0' > 0 && current < j) {
               int diff = j - current;
               needed += diff;
               current += diff;
           }
           current += s[j] - '0';
           // cout << "For " << j;
           // cout << " Current " << current;
           // cout << " Needed " << needed;
           // cout << " Value " << s[j];
           // cout << endl;
        }
        printf("Case #%d: %d\n", i + 1, needed);
    }
    return 0;
}
