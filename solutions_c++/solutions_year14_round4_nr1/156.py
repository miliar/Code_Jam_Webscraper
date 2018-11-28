#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <algorithm>

using namespace std;

int T;
int n;
int x;
vector<int> ss;
vector<bool> bb;

int main()
{
    cin >> T;
    for (int t=1; t<=T; ++t) {
        ss.clear();
        bb.clear();
        cin >> n >> x;
        for (int i=0; i<n; ++i) {
            int s;
            cin >> s;
            ss.push_back(s);
            bb.push_back(false);
        }
        sort(ss.begin(), ss.end());
        int ans = 0;
        for (int i=n-1; i>=0; --i) {
            if (bb[i]) continue;
            for (int j=i-1; j>=0; --j) {
                if (bb[j]) continue;
                if (ss[i] + ss[j] <= x) {
                    bb[i] = true;
                    bb[j] = true;
                    ans++;
                    break;
                }
            }
            if (bb[i] == false) {
                bb[i] = true;
                ans++;
            }
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
