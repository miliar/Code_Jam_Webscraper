#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int main() {
    int T, i, j, k, N, N_temp, icount, dcount;
    bool all_digit[10];
    
    scanf("%d", &T);
    
    for (i = 0; i < T; i++){
        // init
        for(k = 0; k < 10; k++ )
		    all_digit[k] = false;
		    
        icount = 0;
        dcount = 0;
        
        scanf("%d", &N);
        
        if (N == 0) {
            printf("Case #%d: %s\n", i+1, "INSOMNIA");
            continue;
        }
        
        while (dcount < 10) {
            icount++;
            N_temp = N * icount;
            string nstr = to_string(N_temp);
            
            for (j = 0; j < nstr.size(); j++) {
                switch (nstr[j]) {
                    case '0':
                        all_digit[0] = true;
                        break;
                    case '1':
                        all_digit[1] = true;
                        break;
                    case '2':
                        all_digit[2] = true;
                        break;
                    case '3':
                        all_digit[3] = true;
                        break;
                    case '4':
                        all_digit[4] = true;
                        break;
                    case '5':
                        all_digit[5] = true;
                        break;
                    case '6':
                        all_digit[6] = true;
                        break;
                    case '7':
                        all_digit[7] = true;
                        break;
                    case '8':
                        all_digit[8] = true;
                        break;
                    case '9':
                        all_digit[9] = true;
                        break;
                }
            }
                
            dcount = 0;
            for (k = 0; k < 10; k++) {
                if (all_digit[k]) {
                    dcount++;
                }
            }
                
            nstr.clear();
        }
            
        printf("Case #%d: %d\n", i+1, N_temp);
    }
    return 0;
}