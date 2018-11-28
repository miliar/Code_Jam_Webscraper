#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main() {
    int t; cin>>t;
    for(int ti=1;ti<=t;++ti) {
        int n; cin>>n;
        vector<double> wn(n, 0.0);
        vector<double> wk(n, 0.0);
        for(int i=0;i<n;++i) cin>>wn[i];
        for(int i=0;i<n;++i) cin>>wk[i];

        sort(wn.begin(), wn.end());
        sort(wk.begin(), wk.end());

        //for(int i=0;i<n;++i) cerr<<wn[i] << ' '; cerr << endl;
        //for(int i=0;i<n;++i) cerr<<wk[i] << ' '; cerr << endl;

        vector<bool> used(n, false); // for wn
        int win_d = 0;

        int kl =0, kh = n-1;
        for(int i=0;i<n;++i) {
            if(wk[kl] > wn[i]) {
                kh--; 
            }else {
                kl++;
                win_d++;
            }
        }
        //cerr << "war " << endl;
        int lost = 0; kl=0,kh=0;
        for(int i=0;i<n;++i) {
            //while(kl < n && used[kl]) kl++;
            
            while(kh < n && wk[kh] < wn[i]) kh++;
            if(kh < n ) {
                lost++;
                //cerr << wn[i] << ' ' << wk[kh] << endl;
                kh++;
            } else {
                break;
            }
        }
        cout << "Case #"<<ti << ": " ;
        cout << win_d << " " << n-lost << endl;
    }
    return 0;
}
