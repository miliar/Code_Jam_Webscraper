#include <bits/stdc++.h>
using namespace std;

int main(){
    freopen ("P1.in","r",stdin);
    freopen ("P1.out","w",stdout);
	int T;
	scanf ("%d", &T);
	for (int t = 1; t <= T; t++){
        int N, M, I = 1, C, Z;
        scanf ("%d", &N);
        bool nums [10];
        memset(nums, false, sizeof(nums));
        if (N  == 0){ cout << "Case #" << t <<": INSOMNIA" << endl;
            continue;
        }
        while (true){
            C = 0;
            M = N*I;
            I++;
            Z = floor (log10 (abs(M)))+1;
            for (int m = 0; m < Z; m++){
               nums[M%10] = true;
               M /= 10; 
            }    
            for (int n = 0; n < 10; n++){
                C += nums[n];
            }
            if (C == 10) break;
        }
        cout << "Case #" << t << ": "<<N*(I-1) << endl;
    }
    return 0;
}

