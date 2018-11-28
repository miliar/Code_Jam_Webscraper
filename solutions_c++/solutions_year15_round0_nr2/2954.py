#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <cassert>
#include <cstring>
#include <cmath>
#include <fstream>
#include <algorithm>
#include <climits>

using namespace std;

int main()
{
    int t, n;
    ifstream fp ("/Users/aviral.gupta/Downloads/in.txt");
    ofstream ofp ("/Users/aviral.gupta/Downloads/out.txt");
    fp >> t;
    for(int k = 1;k <= t; k++) {
        int sum = 0, a[1005], res = INT_MAX, mp[1005] = {0};
        fp >> n;
        for (int i =0; i < n; i++) {
            fp >> a[i];
            mp[a[i]]++;
        }
        for (int i = 1000; i >= 1; i--) {
            sum = 0;
            for (int j = 0; j < n; j++) {
                if (a[j] > i)
                    sum += ceil ((double) a[j]/ (double)i) - 1;
            }
            if (i + sum < res)
                res = sum + i;
        }
        ofp << "Case #" << k << ": " << res << endl;
    }
    fp.close();
    ofp.close();
    return 0;
}
