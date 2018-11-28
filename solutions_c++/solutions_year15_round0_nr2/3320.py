#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream cin("test.in");
    ofstream cout("test.out");

    int t;
    cin >> t;
    for (int k = 0; k < t; k++) {
        int n, mini = -1, maxi = 0;
        cin >> n;
        int A[n], B[n];
        for (int i = 0; i < n; i++) {
            cin >> A[i];
            maxi = max(A[i], maxi);
        }

        for (int j = 1; j <= maxi; j++) {
            int now = 0;
            for (int ii = 0; ii < n; ii++) {
                if (j < A[ii])
                            now += ((A[ii]-1)/j);
            }
            now += j;
            if (mini == -1) mini = now;
            if (mini > now) mini = now;

        }

        cout << "Case #" << k+1 << ": " << mini << endl;
    }

}
