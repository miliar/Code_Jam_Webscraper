#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
#define MAXN 100

int main() {
    int t; cin>>t;
    for(int ti=1;ti<=t;++ti) {
        int n; cin>>n;
        vector<string> vs;
        
        string seq = "";
        string s;
        bool ok = true;
        vector< vector<int> >rep(MAXN, vector<int>(n, 0));

        for(int i=0;i<n;++i) {
            cin>>s;
            vs.push_back(s);
            int idx = 0;
            for(int j=0;j<s.size() && ok;++j) {
                if(j==0||s[j]!=s[j-1]) {
                    if(i==0) seq += s[j];
                    else if(s[j] != seq[idx]) ok = false;
                    idx++;
                } else {
                    rep[idx-1][i]++;
                }
                //cerr << idx << ' ';
            }
            //cerr << endl;
            if(idx < seq.size()) ok = false;
        }
        cout << "Case #" << ti << ": " ; 
        if(!ok) {
            cout << "Fegla Won" <<endl;
            continue;
        }

        int ans = 0;
        for(int i=0;i<seq.size();++i) {
            sort(rep[i].begin(), rep[i].end());
            // median
            int med = rep[i][n/2];
            //cerr << seq[i] <<" med=" << med<<endl;
            for(int j=0;j<n;++j) {
                ans+= abs(rep[i][j]-med);
            }
        }
        cout << ans << endl;
        
    }
    
    return 0;
}

        
