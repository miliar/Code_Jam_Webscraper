#include<iostream>
#include<utility>
#include<set>
#define pii pair<int, int>

using namespace std;


int main(void) {
    int T; cin >> T;
    int ca=0;
    while(T--) {
        int n; cin >> n;
        set<pii> os;
        
        int N=0;
        for(int i=0; i<n; i++) {
            int x; cin >> x;
            N+=x;
            os.insert({x,i});
        }
        // cout << N << endl;
        cout << "Case #" << ++ca << ": ";
        bool flag = false;
        for(int i=0; i<N;) {
            
            // for(auto x:os) {
            //     cout << x.first << " " << x.second<< endl;
            // }
            if(os.empty()) continue;
            pii p = *(--os.end());
            os.erase(--os.end());
            if(p.first>=2) {
                os.insert({p.first-1,p.second});
            }
            i++;
            cout << (char)('A'+p.second);
            if(N%2==1 && !flag && !os.empty()) {
                // cout << "N: " << N << endl;
                
                // cout << "here" << endl;
                // cout << (*(--os.end())).first << endl;
                // cout << "here2" << endl;
                if((N-i)/2>=(*(--os.end())).first ) {
                    flag = true;
                    cout << " ";
                    continue;
                }
            }
            
            if(os.empty()) continue;
            p = *(--os.end());
            os.erase(--os.end());
            if(p.first>=2) {
                os.insert({p.first-1,p.second});
            }
            i++;
            cout << (char)('A'+p.second) << " ";
        }
        cout << endl;
    }
    
    return 0;
}