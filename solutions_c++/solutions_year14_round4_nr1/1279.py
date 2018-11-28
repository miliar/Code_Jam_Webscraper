#include <cstdio>
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int a[11111];

int main(){
    ifstream input ("A-large.in");
    ofstream output ("output.txt");

    int t, n, x;
    input >> t;

    for (int i = 1; i <= t; i++){
        input >> n >> x;
        for (int ii = 1; ii <= n; ii++) input >> a[ii];

        sort(a + 1, a + n + 1);

        int cnt = 0;
        int j = 1;
        for (int ii = n; ii >= 1; ii--){
            if (j > ii) break;

            if (a[ii] + a[j] <= x){
                cnt++;
                j++;
            }
            else {
                cnt++;
            }
        }

        output << "Case #" << i << ": " << cnt << endl;
    }

    input.close();
    output.close();

    return 0;
}
