#include <iostream>
#include <algorithm>
#include <string>
#include <stdio.h>
#include <cstring>

using namespace std;
    
int main() {
    int T, i, j, k, slen;
    string dat;
    string dat2;
    int d1, d2;
    scanf("%d", &T);
    
    for (i = 0; i < T; i++) {
        dat2 = "";
        cin >> dat;
        slen = strlen(dat.c_str());
        
        if (slen > 0) {
            dat2.insert(dat2.begin(), dat[0]);
            d2 = (int)(dat2[0]);
        } else {
            printf("Case #%d: %s\n", i+1, "No input error");
            return 0;
        }

        for (j = 1; j < slen; j++) {
            d1 = (int)(dat[j]);
            
            if (d2 <= d1) {
                dat2.insert(dat2.begin(), dat[j]);
                d2 = dat[j];
            } else {
                dat2.insert(dat2.end(), dat[j]);
            }
        }
        cout << "Case #" << i+1 << ": " << dat2 << endl;
    }
    return 0;
}