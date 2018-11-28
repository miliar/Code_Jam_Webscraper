#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
    int i, j, k, l, m, n, t, j_f, j_l, k_f, k_l;
    int count;
    cin >> t;
    double a[2000], b[2000];
    for (i = 0; i < t; i++) {
        count = 0;
        cin >> n;
        for (j = 0; j < n; j++) {
            cin >> a[j];
        }
        sort(a, a + n);
        for (j = 0; j < n; j++) {
            cin >> b[j];
        }
        sort(b, b + n);


        //part1
        j_f = 0;
        j_l = n-1;

        k_f = 0;
        k_l = n-1;

        while (j_f <= j_l && a[j_f] < b[0]) {
            j_f++;
            k_l--;
        }
        //part2
        while (k_l >= k_f && a[j_l] < b[k_l]) {
            j_f++;
            k_l--;
        }
        while (j_f <= j_l) {
            if (b[k_f] < a[j_f]) {
                count++;
                k_f++;
            }
            j_f++;
        }
        cout << "Case #" << i+1 << ": " << count << " ";
        j_f = 0;
        j_l = n-1;

        k_f = 0;
        k_l = n-1;
        count = 0;
        while (j_f <= j_l && k_f <= k_l) {
            if (a[j_l] > b[k_l]) {
                j_l--;
                k_f++;
                count++;
            }
            else {
                j_l--;
                k_l--;
            }
        }
        cout << count << endl;
    }
    return 0;
}
