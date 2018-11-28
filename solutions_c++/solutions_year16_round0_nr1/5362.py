#include <iostream>
using namespace std;

int main() {
    int T, N, TT=1;
    int a[10], c, n, threshold = 0, m, oldc;
    cin >> T;
    while (T-->0) {
        cin >> N;
        c=0, n=0, m=0, oldc = -1;
        for (int i=0; i<10; i++) a[i]=0;
        do {
            n+=N;
            m++;
            int t = n;
            while (t>0) {
                int j = t - ((t / 10) * 10);
                t = t / 10;
                if (a[j]==0) {
                    a[j]=1;
                    c++;
                }
            }
            if (oldc == c) threshold++;
            else {
                threshold=0;
                oldc = c;
            }
        } while (c<10 && threshold < 3000);
        if (threshold == 3000)
            cout << "Case #" << TT++ << ": " << "INSOMNIA" << endl;
        else
            cout << "Case #" << TT++ << ": " << n << endl;
    }
}