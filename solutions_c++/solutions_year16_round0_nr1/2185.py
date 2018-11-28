#include <iostream>
using namespace std;

int main(){
    long T, N, curN;
    int digit;
    bool flag[10];

    cin >> T;
    for (int i = 1; i <= T; i++){
        cin >> N;
        cout << "Case #" << i << ": " ;

        if (N == 0){
            cout << "INSOMNIA\n";
            continue;
        }

        int thresh = 1;//, nthresh = 0; // thresh = 10^nthresh
        int k = 0, step = 1;
        int count = 10;
        for (int j = 0; j <= 9; j++) flag[j] = false;

        curN = 0;
        while (count > 0){
            k += step;
            curN += step * N;

            // judge digits
            int n = curN;
            while (n > 0){
                // while curN is 10...0, there is unecessary loop on 0
                // but it is trivial in time complexity
                digit = n % 10;
                if (!flag[digit]){
                    flag[digit] = true;
                    count--;
                }
                n /= 10;
            }

            // update threshold and step
            while (curN > thresh){
                thresh *= 10;
                //nthresh++;
            }
            if (curN == thresh){ //10...0
                step = curN / N;
            }
        }

        cout << curN << endl;

    }
}
