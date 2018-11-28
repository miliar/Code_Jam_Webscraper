#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        int N;
        cin >> N;
        cout << "Case #" << t << ": ";
        int zero = 0;
        int num = N;
        while(N%10 == 0 && N) {
            zero = 1;
            N /= 10;
        }
        if(N == 0) {
            cout << "INSOMNIA\n";
            continue;
        }
        N = num;
        int hs[10] = {0};
        hs[0] = zero;
        int ans = N;
            int flg = 1;
            for(int i=1; i<= 200; i++) {
                N = num*i;
                int nu = N;
				while(nu) {hs[nu%10] = 1;  nu /= 10;}


                for(int j=0; j<10; j++) {   if(hs[j] == 0) {    flg = 0;    break;  }   }

                if(flg == 1) {
                    ans = N;
                    break;
                }
                if(flg == 0 && i == 200)
                    flg = 0;
                else flg = 1;
            }
            if(flg == 0) {
                ans = -1;
            }
        if(ans == -1) {
            cout << "INSOMNIA\n";
        } else {
            cout << ans << endl;
        }
    }
}
