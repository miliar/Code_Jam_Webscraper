#include<iostream>
using namespace std;

void init0(bool arr[], int n) {
    for (int i=0 ; i<n ; i++)
        arr[i] = 0;
}

main() {
    int t;
    cin >> t;
    for (int c=1 ; c<=t ; c++) {
        long long int n, n2;
        cin >> n;
        cout << "Case #" << c << ": ";
        if (n==0) {
            cout << "INSOMNIA\n";
            continue;
        }
        bool dig[10];
        int digs=0, k=n;
        init0(dig, 10);
        while (digs<10) {
            long long int temp = n;
            int currdig;
            while (temp > 0) {
                currdig = temp%10;
                temp /= 10;
                if (dig[currdig]==0) {
                    digs++;
                    dig[currdig] = 1;
                }
            }
            n2 = n;
            n += k;
        }
        cout << n2 << endl;
    }
}
