#include <iostream>
#include <iomanip>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;
typedef long long ll;



int main(){
    int T;
    cin >> T;
    for(int t=1;t<=T;t++){
        int N, K;
        
        cin >> N >> K;
        
        vector<int> sums(N-K+1);
        for(int i=0;i<N-K+1;i++) cin >> sums[i];
        vector<int> diffs(N-K);
        for(int i=0;i<N-K;i++) diffs[i] = sums[i+1]-sums[i];
        
        
        
        int modsum = sums[0];
        int best = 0;
        
        vector<int> lengths(K);
        for(int i=0;i<K;i++){
            int cmin = 0;
            int cmax = 0;
            int cur = 0;
            for(int j=i;j<N-K;j+=K){
                cur+=diffs[j];
                if(cur<cmin) cmin = cur;
                if(cur>cmax) cmax = cur;
            }
            
            modsum+=cmin;
            
            if(cmax-cmin>best){
                best = cmax-cmin;
            }
            
            lengths[i] = cmax-cmin;
            
        }
        
        int raise = ((modsum%K)+K)%K;
        
        int excess = 0;
        for(int i=0;i<K;i++) excess+=(best-lengths[i]);
//        cout << modsum << " " << raise << " " << nlargest << endl;
        if(raise > excess) best++;
        
        cout << "Case #" << t << ": " << best << endl;
        
    }

    return 0;
}