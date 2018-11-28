/*
Input 
 	
4
1
0.5
0.6
2
0.7 0.2
0.8 0.3
3
0.5 0.1 0.9
0.6 0.4 0.3
9
0.186 0.389 0.907 0.832 0.959 0.557 0.300 0.992 0.899
0.916 0.728 0.271 0.520 0.700 0.521 0.215 0.341 0.458



Output 
 
Case #1: 0 0
Case #2: 1 0
Case #3: 2 1
Case #4: 8 4
*/

#include <sstream>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdint>

#include <vector>
#include <list>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <deque>
#include <set>

#include <string>

#include <stdint.h>
#include <limits>

using namespace std;
typedef pair<int, int> pii;
typedef long long ll;

void dumpa(int* a, int n) {
    for (int i = 0; i < n; i++) 
        printf("%4d", a[i]);
    printf("\n");
}
int main() {
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    int N;
    cin >> N;
    int i = 0;

    while (i++ < N) {
        int n;
        int y = 0, z = 0;
        double naomi[10] = {0}, ken[10] = {0};
        cin >> n;
        for (int j = 0; j < n; j++)
            cin >> naomi[j];
        for (int j = 0; j < n; j++)
            cin >> ken[j];
        sort(naomi, naomi + n);
        sort(ken, ken + n);
        double n2[10], k2[10];
        memcpy(n2, naomi, sizeof(naomi));
        memcpy(k2, ken, sizeof(ken));
        //get z first which is easier :)

        for (int j = n-1; j >= 0; j--) {
            int k = 0;
            while (k2[k] < n2[j] && k <= j) k++;
            if (k > j) {
                k2[0] = k2[j];
                sort(k2, k2 + j);
                z++;
            } else {
                k2[k] = k2[j];
                sort(k2, k2 + j);
            }
        }

        for (int j = 0; j < n; j++) {
            double t = naomi[j];
            //check whether able to lose or win
            if (naomi[n-1-j] < ken[n-1-j]) {
                naomi[0] = naomi[n-1-j];
                sort (naomi, naomi + (n-1-j));
            } else if (naomi[0] < ken[0]) {
                naomi[0] = naomi[n-1-j];
                sort (naomi, naomi + (n-1-j));
            } else {
                naomi[0] = naomi[n-1-j];
                sort (naomi, naomi + (n-1-j));
                ken[0] = ken[n-1-j];
                sort(ken, ken + (n-1-j));
                y++;
            }
        }


        cout << "Case #" << i << ": " << y << " " << z << endl;
    }
}
