// Coded by HACKER_J

#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <iterator>

using namespace std;

int main() {
    int T, i, j, k, slen, ok_ind, fp_ind, fm_ind, flip_count;
    char dat[105];
    
    scanf("%d", &T);
    
    for (i = 0; i < T; i++){
        scanf("%s", dat);
        slen = strlen(dat);
        ok_ind = slen;
        
        for (j = slen - 1; j >= 0; j--) {
            if (dat[j] == '+') {
                ok_ind--;
            } else {
                break;
            }
        }
        
        if (ok_ind == 0) {
            printf("Case #%d: %d\n", i+1, 0);
            continue;
        }
        
        slen = ok_ind;
        flip_count = 0;
        
        while (ok_ind > 0) {
            
            if (dat[0] == '+') {
                fp_ind = 1;
                for (k = 1; k < ok_ind; k++) {
                    if (dat[k] == '+') {
                        fp_ind++;
                    } else {
                        break;
                    }
                }
                
                reverse(begin(dat), begin(dat) + fp_ind);
                for (k = 0; k < fp_ind; k++) {
                    if (dat[k] == '+') {
                        dat[k] = '-';
                    } else {
                        dat[k] = '+';
                    }
                }
                flip_count++;
            } else {
                fm_ind = 1;
                for (k = 1; k < ok_ind; k++) {
                    if (dat[k] == '-') {
                        fm_ind++;
                    } else {
                        break;
                    }
                }
                
                reverse(begin(dat), begin(dat) + fm_ind);
                for (k = 0; k < fm_ind; k++) {
                    if (dat[k] == '+') {
                        dat[k] = '-';
                    } else {
                        dat[k] = '+';
                    }
                }
                flip_count++;
            }
            
            for (j = slen - 1; j >= 0; j--) {
                if (dat[j] == '+') {
                    ok_ind--;
                } else {
                    break;
                }
            }
            slen = ok_ind;
        }
        
        printf("Case #%d: %d\n", i+1, flip_count);
    }
    return 0;
}