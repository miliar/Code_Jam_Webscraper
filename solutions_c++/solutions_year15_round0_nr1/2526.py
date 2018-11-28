#include <iostream>
using namespace std;
int main() {
    int t;
    cin>>t;
    for(int xx = 0; xx < t; ++xx) {
        int smax;
        string s;
        cin>>smax>>s;
        int lo = 0;
        int hi = 1e3+10;
        int best = hi;
        while(lo <= hi) {
            int mid = (lo+hi)/2;
            int cnt = mid;
            for(int i = 0; i <= smax; ++i) {
                if(i > cnt) goto ohi;
                cnt += s[i] - '0';
            }
            hi = mid-1;
            best = mid;
            continue;
            ohi:;
            lo = mid+1;
        }
        cout<<"Case #"<<xx+1<<": "<<best<<'\n';

    }
}
