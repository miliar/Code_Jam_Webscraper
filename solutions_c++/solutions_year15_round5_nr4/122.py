#include <iostream>
using namespace std;
const int MN = 1e5;
int t[MN];
int f[MN];
int cnt[(int)1e8+10];
int getFirst() {
    for(int i = 0; i < MN; ++i) {
        if(cnt[t[i]] > 0) return i;
    }
    return -1;
}
int main() {
    int tt;
    cin>>tt;
    for(int xx = 1; xx <= tt; ++xx) {
        int p;
        cin>>p;
        int n = 0;

        int sum = 0;
        for(int i = 0; i < p; ++i) {
            cin>>t[i];
        }
        for(int i = 0; i < p; ++i) {
            cin>>f[i];
            sum += f[i];
            cnt[t[i]] += f[i];
        }
        for(int i = 0; i < 100; ++i) {
            if(1<<i == sum) {
                n = i;
                break;
            }
        }
        int ans[MN] = {0};
        --f[0];
        --cnt[0];
        for(int i = 0; i < n; ++i) {
            int q = t[getFirst()];
            //cout<<"LOl\n";
            //cout<<q<<'\n';
            ans[i] = q;
            if(i) {
                for(int j = 0; j < (1<<i); ++j) {
                    int sum = 0;
                    for(int k = 0; k < i; ++k) {
                        if(j & (1<<k)) {
                            sum += ans[k];
                        }
                    }
            //        cout<<sum+q<<'\n';
                    cnt[sum+q]--;
                }
            }
            else {
                cnt[q]--;
            }
        }
        cout<<"Case #"<<xx<<": ";
        for(int i = 0; i < n; ++i) {
            cout<<ans[i]<<' ';
        }
        cout<<'\n';
    }
}
