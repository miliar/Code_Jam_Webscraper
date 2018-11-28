#include <iostream>
using namespace std;
int main()
{

    int i, j, n, k, t;
    int a[] = {1,4,9,121,484};
    cin >> n;
    for (i = 0; i < n; i++) {
        int count = 0;
        cin >> j >> k;
        for (t = 0; t < 5; t++) {
            if (a[t] >= j && a[t] <= k) {
                    count++;
            }

        }
        cout << "Case #" << i+1 << ": " << count << endl;
    }
    return 0;
}
