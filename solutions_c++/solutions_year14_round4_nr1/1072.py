#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

int main() {
    int T;
    cin>>T;
    for (int t=1;t<=T;++t) {
        int N, X;
        cin>>N>>X;
        vector<int> v;
        for (int i=0;i<N;++i) {
            int a;
            cin>>a;
            v.push_back(a);
        }

        sort(v.begin(), v.end());

        int ans = 0;
        int s = 0;
        for (int e=v.size()-1; e>=s; ) {
            if ( e == s) {
                ans++;
                break;
            }
            if (v[e] + v[s] <= X) {
                ans++;
                e--;
                s++;
            } else {
                ans++;
                e--;
            }
        }

        printf("Case #%d: %d\n", t, ans);
    }
}
